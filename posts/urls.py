from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = [
    path('api/1.0/', include(router.urls)),
]