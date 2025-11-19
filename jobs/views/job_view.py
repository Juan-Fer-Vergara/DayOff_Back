from rest_framework import viewsets, filters
from jobs.models import Job
from jobs.serializers.job_serializer import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer

    # Filtros por categoría, empresa, lugar, rango salarial
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['created_at', 'salary']

    def get_queryset(self):
        queryset = Job.objects.all()

        # FILTRO por category_id
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        # FILTRO por company_id
        company_id = self.request.query_params.get('company')
        if company_id:
            queryset = queryset.filter(company_id=company_id)

        # FILTRO por localización
        location = self.request.query_params.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset.order_by('-created_at')
