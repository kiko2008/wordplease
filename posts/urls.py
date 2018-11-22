from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet
from posts.views import HomeView, PostDetailView, NewPostView

router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('blogs/<int:blog_id>/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('new-post', NewPostView.as_view(), name='new-post'),

    # API REST
    path('api/1.0/', include(router.urls)),
]