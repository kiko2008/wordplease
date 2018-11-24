from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blogs.api import BlogViewSet
from blogs.views import BlogsView, BlogDetailView, NewBlogView

router = DefaultRouter()
router.register('blogs', BlogViewSet)

urlpatterns = [
    path('blogs', BlogsView.as_view(), name='blogs'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('new-blog', NewBlogView.as_view(), name='new-blog'),

    # API REST
    path('api/1.0/', include(router.urls)),
]
