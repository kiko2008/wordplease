from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet
from posts.views import HomeView

router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),

    # API REST
    path('api/1.0/', include(router.urls)),
]