from rest_framework import permissions

class IsAdminOrCompanyOwner(permissions.BasePermission):
    """
    Admin: todo.
    Company: solo aplicaciones de sus trabajos.
    User: solo sus aplicaciones (ya se maneja en get_queryset).
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == "ADMIN":
            return True

        if user.role == "COMPANY":
            return obj.job.company.id == user.company.id  # si usas FK empresa → usuario

        if user.role == "USER":
            return obj.user == user

        return False
