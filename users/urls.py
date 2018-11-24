from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet
from users.views import LoginView, LogoutView, LogupView

router = DefaultRouter()
router.register('users', UserViewSet, base_name='users')

urlpatterns = [

    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('logup', LogupView.as_view(), name='logup'),

    # API REST
    path('api/1.0/', include(router.urls)),
]