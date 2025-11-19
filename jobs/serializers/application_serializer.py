# from rest_framework import serializers
# from jobs.models import Application
# from jobs.serializers.job_serializer import JobSerializer
# from django.conf import settings

# class ApplicationSerializer(serializers.ModelSerializer):
#     job_data = JobSerializer(source="job", read_only=True)
#     user = serializers.PrimaryKeyRelatedField(
#         queryset=settings.AUTH_USER_MODEL.objects.all()
#     )

#     class Meta:
#         model = Application
#         fields = [
#             "id",
#             "job",
#             "job_data",
#             "user",
#             "cover_letter",
#             "cv",
#             "status",
#             "created_at"
#         ]
#         read_only_fields = ["status", "created_at"]

from rest_framework import serializers
from jobs.models import Application
from jobs.serializers.job_serializer import JobSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ApplicationSerializer(serializers.ModelSerializer):
    job_data = JobSerializer(source="job", read_only=True)
    
    # El usuario se asigna desde la vista, no desde el cliente
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = [
            "id",
            "job",
            "job_data",
            "user",
            "cover_letter",
            "cv",
            "status",
            "created_at"
        ]
        read_only_fields = ["status", "created_at"]
