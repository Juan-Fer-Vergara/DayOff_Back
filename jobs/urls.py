from django.urls import path, include
from rest_framework.routers import DefaultRouter
from jobs.views.job_view import JobViewSet
from jobs.views.category_view import CategoryViewSet
from jobs.views.company_view import CompanyViewSet
from jobs.views.application_view import ApplicationViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='jobs')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'companies', CompanyViewSet, basename='companies')
router.register(r'applications', ApplicationViewSet, basename='applications')

urlpatterns = [
    path('', include(router.urls)),
]
