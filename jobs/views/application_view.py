from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from jobs.models import Application, Job
from jobs.serializers.application_serializer import ApplicationSerializer
from rest_framework.decorators import action


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # 1️⃣ ADMIN: ve todo
        if user.is_staff or user.role == "ADMIN":
            return Application.objects.all()

        # 2️⃣ COMPANY_OWNER: ver solo postulaciones a sus propios Jobs
        if user.role == "COMPANY_OWNER":
            return Application.objects.filter(job__company__owner=user)

        # 3️⃣ JOB_SEEKER: ve solo las suyas
        return Application.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        job = serializer.validated_data.get("job")

        # Evitar que Company Owners se postulen
        if user.role == "COMPANY_OWNER":
            raise ValidationError("Los dueños de empresas no pueden postularse a trabajos.")

        # Evitar que alguien se postule dos veces al mismo job
        if Application.objects.filter(user=user, job=job).exists():
            raise ValidationError("Ya te has postulado a este trabajo.")

        # Asignar usuario automáticamente
        serializer.save(user=user)

    # -------------------------
    #  A C C I Ó N — A C E P T A R
    # -------------------------
    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        application = self.get_object()
        user = request.user

        # Solo Company Owner que sea dueño del Job
        if user.role != "COMPANY_OWNER":
            return Response({"detail": "No autorizado"}, status=403)

        if application.job.company.owner != user:
            return Response({"detail": "No puedes modificar postulaciones de otra empresa."}, status=403)

        application.status = "accepted"
        application.save()

        return Response(
            {"detail": "Postulación aceptada", "status": application.status},
            status=status.HTTP_200_OK
        )

    # -------------------------
    #  A C C I Ó N — R E C H A Z A R
    # -------------------------
    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        application = self.get_object()
        user = request.user

        # Solo Company Owner
        if user.role != "COMPANY_OWNER":
            return Response({"detail": "No autorizado"}, status=403)

        if application.job.company.owner != user:
            return Response({"detail": "No puedes modificar postulaciones de otra empresa."}, status=403)

        application.status = "rejected"
        application.save()

        return Response(
            {"detail": "Postulación rechazada", "status": application.status},
            status=status.HTTP_200_OK
        )