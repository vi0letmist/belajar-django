from rest_framework.exceptions import PermissionDenied
from rest_framework import permissions
from belajar_django.constants import UNAUTHORIZED_MESSAGE


class CustomIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        
        if not request.user.is_authenticated:
            raise PermissionDenied(UNAUTHORIZED_MESSAGE)

        if request.user.role not in ['Admin', 'Librarian']:
            raise PermissionDenied(UNAUTHORIZED_MESSAGE)
        
        return True
class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if not request.user.is_authenticated:
            raise PermissionDenied(UNAUTHORIZED_MESSAGE)

        if request.user.role not in ['Admin', 'Librarian']:
            raise PermissionDenied(UNAUTHORIZED_MESSAGE)
        
        return True
