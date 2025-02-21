from rest_framework import generics, permissions

from django.contrib.auth import get_user_model
from .serializers import ThreadSerializer, CommentSerializer, CustomUserSerializer, LikeSerializer
from forum.models import Thread, Comment, Like


class ThreadRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class ThreadListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CustomUserListAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAdminUser, )
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
