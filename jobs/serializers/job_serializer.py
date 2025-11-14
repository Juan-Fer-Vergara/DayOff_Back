from rest_framework import serializers
from jobs.models import Job
from .category_serializer import CategorySerializer
from .company_serializer import CompanySerializer

class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
