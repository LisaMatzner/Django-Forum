from rest_framework import serializers
from django.contrib.auth import get_user_model
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
        model = get_user_model()
        fields = ["id", "username", "display_name"]


class LikeSerializer(serializers.ModelSerializer):
    thread_title = serializers.SerializerMethodField()
    class Meta:
        model = Like
        fields = ["liked_by", "comment", "thread_title"]

    def get_thread_title(self, obj):
        return obj.comment.thread.title
