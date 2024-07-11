from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Blog, Comment, Like
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAdminOrReadOnly]


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LikeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def create(self, request):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            l_value = serializer.validated_data.get('like')
            d_value = serializer.validated_data.get('dislike')
            blog_id = serializer.validated_data.get('blog')
            blog = Blog.objects.get(pk=blog_id)

            try:
                like = Like.objects.get(
                    blog=blog,
                    user=request.user
                )
                like.delete()
            except Like.DoesNotExist:
                like_or_dislike = True if l_value else False
                Like.objects.create(
                    blog=blog,
                    user=request.user,
                    like_or_dislike=like_or_dislike
                )
            return Response({'success': "Muvofaqiyatli!!!"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def list(self, request):
        serializer = LikeSerializer()
        return Response(serializer.data)