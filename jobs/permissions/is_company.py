from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from .roles import ROLE_COMPANY

User = get_user_model()

class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == ROLE_COMPANY)
