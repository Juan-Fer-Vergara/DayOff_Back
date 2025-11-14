from rest_framework import viewsets
from jobs.models import Category
from jobs.serializers.category_serializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
