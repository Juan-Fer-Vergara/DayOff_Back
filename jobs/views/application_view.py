from rest_framework import viewsets, permissions
from jobs.models import Application
from jobs.serializers.application_serializer import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Application.objects.all()

        return Application.objects.filter(user=user)
