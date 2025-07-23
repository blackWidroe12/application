from rest_framework import viewsets, permissions
from rest_framework_gis.filters import InBBoxFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import InfrastructureFilter, WardFilter
from .serializers import (
    UserSerializer,
    InfrastructureSerializer,
    RoadSerializer,
    BuildingSerializer,
    WardGeoSerializer
)
from infrastructure.models.spatial import Infrastructure, Road, Building
from infrastructure.models.core import Ward
from infrastructure.models.user import User
from utils.permissions import (
    IsAdminOrReadOnly,
    IsOwnerOrAdmin,
    WardBasedPermission
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.prefetch_related('wards')
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['role', 'wards__id']

class InfrastructureViewSet(viewsets.ModelViewSet):
    permission_classes = [WardBasedPermission]
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    bbox_filter_field = 'geom'
    bbox_filter_include_overlapping = True
    filterset_class = InfrastructureFilter

    def get_queryset(self):
        qs = Infrastructure.objects.select_related('type', 'ward')
        if not self.request.user.is_staff:
            qs = qs.filter(ward__in=self.request.user.wards.all())
        return qs

    def get_serializer_class(self):
        if self.action == 'retrieve':
            instance = self.get_object()
            if isinstance(instance, Road):
                return RoadSerializer
            elif isinstance(instance, Building):
                return BuildingSerializer
        elif self.action == 'list':
            # Optionally, you could return a more generic serializer for list
            return InfrastructureSerializer
        return InfrastructureSerializer

class RoadViewSet(InfrastructureViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class BuildingViewSet(InfrastructureViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class WardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardGeoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WardFilter
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]