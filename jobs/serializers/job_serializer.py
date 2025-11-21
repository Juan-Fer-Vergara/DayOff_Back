from rest_framework import serializers
from jobs.models import Job, Category, Company
from jobs.serializers.category_serializer import CategorySerializer
from jobs.serializers.company_serializer import CompanySerializer

class JobSerializer(serializers.ModelSerializer):
    # Solo lectura (GET) para mostrar detalles completos
    category_data = CategorySerializer(source='category', read_only=True)
    company_data = CompanySerializer(source='company', read_only=True)

    # Escritura mediante IDs
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all()
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'description',
            'salary',
            'location',
            'category',       # <- se envía ID aquí
            'company',        # <- se envía ID aquí
            'category_data',  # <- datos completos (solo lectura)
            'company_data',   # <- datos completos (solo lectura)
            'created_at',
        ]
