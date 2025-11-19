from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
    """
    Permite acceso solo a usuarios con rol employer.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "employer"
