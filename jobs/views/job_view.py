from rest_framework import viewsets
from jobs.models import Job
from jobs.serializers.job_serializer import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
