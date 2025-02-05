from django.urls import path
from .views import (
    ThreadListView,
    ThreadDetailView,
    ThreadCreateView,
    ThreadUpdateView,
    ThreadDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    path('threads/', ThreadListView.as_view(), name='threads'),
    path('threads/<int:pk>/', ThreadDetailView.as_view(), name='thread'),
    path('threads/create/', ThreadCreateView.as_view(), name='thread_create'),
    path('threads/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread_update'),
    path('threads/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread_delete'),
    path('threads/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
