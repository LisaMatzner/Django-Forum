from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm

User = get_user_model()

class UserAuthenticationTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
    
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)
    
    def test_register_view_post_valid(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'display_name': 'New User',
            'email': 'newuser@example.com',
            'password1': 'ComplexPass123',
            'password2': 'ComplexPass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('threads'))
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_register_view_post_invalid(self):
        response = self.client.post(reverse('register'), {
            'username': '',
            'password1': 'ComplexPass123',
            'password2': 'DifferentPass456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertFalse(User.objects.filter(username='').exists())
    
    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
    
    def test_login_view_post_valid(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('threads'))
        self.assertTrue('_auth_user_id' in self.client.session)
    
    def test_login_view_post_invalid(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertFalse('_auth_user_id' in self.client.session)
    
    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertFalse('_auth_user_id' in self.client.session)
