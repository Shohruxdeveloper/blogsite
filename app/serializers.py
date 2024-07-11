from rest_framework import serializers
from .models import Blog, Like, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'author', 'created_at', 'updated_at')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'blog', 'created_at', 'updated_at')


class LikeSerializer(serializers.Serializer):
    lesson = serializers.IntegerField()
    like = serializers.BooleanField()
    dislike = serializers.BooleanField()