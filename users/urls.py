from django.urls import path
from .views import TestUserView

urlpatterns = [
    path('test/', TestUserView.as_view(), name='users_test'),
]
