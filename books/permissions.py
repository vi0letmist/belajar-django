# books/permissions.py
from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from belajar_django.constants import UNAUTHORIZED_MESSAGE

class IsAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users with specific roles.
    """
    def has_permission(self, request, view):
        # Ensure the user is authenticated
        if not request.user.is_authenticated:
            raise PermissionDenied(UNAUTHORIZED_MESSAGE)  # Use the global message

        # Check if the user has the required role (Admin or Librarian)
        if request.user.role not in ['Admin', 'Librarian']:
            raise PermissionDenied(UNAUTHORIZED_MESSAGE)
        
        return True
