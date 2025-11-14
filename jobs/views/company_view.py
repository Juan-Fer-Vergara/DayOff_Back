from rest_framework import viewsets
from jobs.models import Company
from jobs.serializers.company_serializer import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
