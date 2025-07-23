from rest_framework import permissions
from infrastructure.models.core import Ward

class WardBasedPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if hasattr(obj, 'ward'):
            return obj.ward in request.user.wards.all()
        if isinstance(obj, Ward):
            return obj in request.user.wards.all()
        return False

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or
            request.user.role == 'admin'
        )

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == 'admin' or
            obj == request.user
        )