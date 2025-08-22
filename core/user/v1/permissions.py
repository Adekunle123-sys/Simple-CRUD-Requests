from rest_framework import permissions

class IsAdminOrReaOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        
class IsUserOrAdmin(permissions.BasePermission):
    """For models with a .user field """
    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user or request.user.is_staff)
    
    
class IsSelfOrAdmin(permissions.BasePermission):
    """For User model only."""
    def has_object_permission(self, request, view, obj):
        return bool(obj == request.user or request.user.is_staff)
