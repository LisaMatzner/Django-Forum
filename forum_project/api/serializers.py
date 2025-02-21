from rest_framework import serializers

from django.conf import settings
from forum.models import Thread, Comment, Like


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ["id", "username", "display_name"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["liked_by", "comment"]
