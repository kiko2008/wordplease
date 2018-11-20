from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from users.permissions import UserPermission
from users.serializer import UserSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]