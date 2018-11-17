from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, base_name='users')

urlpatterns = [
    path('api/1.0/', include(router.urls)),
]