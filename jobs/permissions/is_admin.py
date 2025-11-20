from rest_framework.permissions import BasePermission
from .roles import ROLE_ADMIN

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == ROLE_ADMIN)
