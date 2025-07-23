from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from infrastructure.models.spatial import Infrastructure
from infrastructure.api.serializers import InfrastructureSerializer
import logging

# Get logger instance
logger = logging.getLogger(__name__)

class OfflineSyncView(APIView):
    """API endpoint for syncing offline edits with conflict resolution"""
    
    def post(self, request, format=None):
        edits = request.data.get('edits', [])
        results = []
        
        # Validate input format
        if not isinstance(edits, list):
            return Response(
                {'error': 'Edits must be provided as a list'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            with transaction.atomic():
                for edit in edits:
                    result = self.process_edit(edit, request)
                    results.append(result)
                    
        except Exception as e:
            logger.error(f"Transaction failed: {str(e)}")
            return Response(
                {'error': 'Database transaction failed', 'details': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return Response({'results': results}, status=status.HTTP_207_MULTI_STATUS)
    
    def process_edit(self, edit, request):
        """Process a single offline edit"""
        try:
            # Validate edit structure
            if 'feature_id' not in edit or 'data' not in edit:
                return {
                    'id': edit.get('id', 'unknown'),
                    'status': 'error',
                    'message': 'Missing feature_id or data in edit'
                }
            
            feature_id = edit['feature_id']
            edit_data = edit['data']
            edit_id = edit.get('id', 'unknown')
            
            # Parse and validate timestamp
            edit_ts = self.parse_timestamp(edit.get('timestamp'))
            
            # Retrieve feature with row-level locking
            feature = Infrastructure.objects.select_for_update().get(pk=feature_id)
            
            # Conflict detection
            if edit_ts and feature.updated_at > edit_ts:
                return {
                    'id': edit_id,
                    'status': 'conflict',
                    'message': 'Newer version exists on server',
                    'server_version': feature.updated_at.isoformat()
                }
            
            # Process update
            serializer = InfrastructureSerializer(
                feature,
                data=edit_data,
                partial=True,
                context={'request': request}
            )
            
            if serializer.is_valid():
                try:
                    serializer.save()
                    # Refresh to get updated_at from database
                    feature.refresh_from_db()
                    return {
                        'id': edit_id,
                        'status': 'success',
                        'feature_id': feature_id,
                        'updated_at': feature.updated_at.isoformat()
                    }
                except ValidationError as e:
                    return {
                        'id': edit_id,
                        'status': 'validation_error',
                        'errors': e.message_dict
                    }
            else:
                return {
                    'id': edit_id,
                    'status': 'validation_error',
                    'errors': serializer.errors
                }
                
        except Infrastructure.DoesNotExist:
            return {
                'id': edit_id,
                'status': 'error',
                'message': f"Feature {feature_id} does not exist"
            }
            
        except Exception as e:
            logger.error(f"Error processing edit {edit_id}: {str(e)}")
            return {
                'id': edit_id,
                'status': 'error',
                'message': 'Internal server error',
                'details': str(e)
            }
    
    def parse_timestamp(self, timestamp):
        """Parse and validate timestamp input"""
        if not timestamp:
            return None
            
        if isinstance(timestamp, str):
            parsed = parse_datetime(timestamp)
            if not parsed:
                raise ValidationError('Invalid timestamp format. Use ISO 8601.')
            return parsed
            
        if isinstance(timestamp, (int, float)):
            return timezone.datetime.fromtimestamp(timestamp, timezone.utc)
            
        if isinstance(timestamp, timezone.datetime):
            return timestamp
            
        raise ValidationError('Unsupported timestamp format')