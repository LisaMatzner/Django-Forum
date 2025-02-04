from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #  display_name, number od posts, days_since_join (calculation), 
    display_name = models.CharField(max_length=150, unique=True)
    number_of_posts = models.IntegerField(default=0)

    def __str__(self):
        return self.display_name

