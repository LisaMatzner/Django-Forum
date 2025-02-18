from django.urls import path
from .views import (
    RegisterView, 
    LoginView, 
    LogoutView, 
    UserProfileView,
    EditUserView,
    DeleteUserView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('profile/edit/<str:username>', EditUserView.as_view(), name='edit-user'),
    path('profile/delete/<str:username>', DeleteUserView.as_view(), name='delete-user'),
]
