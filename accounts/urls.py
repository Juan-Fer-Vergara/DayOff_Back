from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
