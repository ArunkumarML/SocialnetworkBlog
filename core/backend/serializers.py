from rest_framework import serializers
from core.models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    parent_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'parent_comment']


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = BlogPost
        fields = ['id', 'title','content', 'author', 'comments','likes']

