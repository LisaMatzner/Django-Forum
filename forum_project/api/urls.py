from django.urls import path

from . import views


urlpatterns = [
    path("threads/", views.ThreadListCreateAPIView.as_view(), name="thread_list"),
    path("threads/<int:pk>/", views.ThreadRetrieveUpdateDestroyAPIView.as_view(), name="thread_detail"),
    path("comments/", views.CommentListCreateAPIView.as_view(), name="comment_list"),
    path("comments/<int:pk>/", views.CommentRetrieveUpdateDestroyAPIView.as_view(), name="comment_detail"),
    path("likes/", views.LikeListAPIView.as_view(), name="like_list"),
    path("likes/<int:pk>/", views.LikeRetrieveAPIView.as_view(), name="like_detail"),
    path("users/", views.CustomUserListAPIView.as_view(), name="user_list"),
    path("users/<int:pk>", views.CustomUserRetrieveAPIView.as_view(), name="user_detail"),
]
