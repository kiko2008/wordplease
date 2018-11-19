from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users.permissions import UserPermission
from users.serializer import UserSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    # def retrieve(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     self.check_object_permissions(request, user)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def update(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     self.check_object_permissions(request, user)
    #     # En lugar de implementar el metodo path, permitimos los partial_update en el verbo put.
    #     # Decido hacerlo asi porque en las apis rest que e implmentado en otros lenguajes nunca me piden implementar el verbo patch,
    #     # en cambio siempre piden que el put permita actualizaciones parciales.
    #     serializer = UserSerializer(user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def destroy(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     self.check_object_permissions(request, user)
    #     user.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
