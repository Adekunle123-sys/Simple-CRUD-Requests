from rest_framework import permissions

class IsAdminOrReaOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        
class IsUserOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = obj.user == request.user
        is_admin=request.user and request.user.is_staff
        return bool(is_owner or is_admin)