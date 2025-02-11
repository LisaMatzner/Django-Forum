from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomUserChangeForm  
from .models import CustomUser
from forum.models import Thread


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()  
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('threads')  
        return render(request, 'users/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            user = form.get_user()  
            login(request, user)  
            return redirect('threads')  
        return render(request, 'users/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)  
        return redirect('login')  


class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'profile_user'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_object(self):
        """Retrieve the user based on the username in the URL.
        no need to pass pk or slug in URL"""
        return get_object_or_404(CustomUser, username=self.kwargs['username'])

    def get_context_data(self, **kwargs):
        """Add the user's threads to context"""
        context = super().get_context_data(**kwargs)
        
        if self.object == self.request.user:
            # If it's the logged-in user, get threads they've created
            context['user_threads'] = Thread.objects.filter(author=self.request.user)
        else:
            # If it's another user's profile, get threads they've created
            context['user_threads'] = Thread.objects.filter(author=self.object)
        
        return context


class EditUserView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'users/edit_user.html'
    context_object_name = 'user'
    form_class = CustomUserChangeForm

    def get_object(self):
        """Return the logged-in user object"""
        return self.request.user

    def get_success_url(self):
        """Redirect to the user's profile page after successful edit"""
        return reverse_lazy('user-profile', kwargs={'username': self.object.username})


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete_user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('threads')

    def get_object(self):
        """Get the logged-in user object to delete"""
        return self.request.user