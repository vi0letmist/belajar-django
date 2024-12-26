from rest_framework import permissions

class IsAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to access an API.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
