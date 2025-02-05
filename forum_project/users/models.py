from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #  display_name, number_of_posts
    display_name = models.CharField(max_length=150, default='username')
    number_of_posts = models.IntegerField(default=0)

    def __str__(self):
        return self.display_name

