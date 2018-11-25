from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from posts.models import Post, Category
from posts.permissions import PostPermission
from posts.serializer import PostSerializer, PostImageFeaturedSerializer


class PostViewSet(GenericViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, PostPermission]

    def retrieve(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        # post object para pasar al check_object_permission en la creacion
        post = Post()
        post.blog_id = request.data.get('blog')
        self.check_object_permissions(request, post)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        # En lugar de implementar el metodo path, permitimos los partial_update en el verbo put.
        # Decido hacerlo asi porque en las apis rest que e implmentado en otros lenguajes
        # nunca me piden implementar el verbo patch, en cambio siempre piden que el put permita
        # actualizaciones parciales.
        serializer = PostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostImageFeaturedViewSet(GenericViewSet):

    parser_classes = (MultiPartParser, FormParser)

    def create(self, request):
        serializer = PostImageFeaturedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

