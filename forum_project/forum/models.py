from django.db import models
from django.conf import settings


# Create your models here.

class Thread(models.Model):
    FLAG_CHOICES = [("d", "default"), ("c","closed"), ("s" ,"sticky"), ("n" ,"new")]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_opened_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    flag = models.CharField(choices=FLAG_CHOICES, max_length=20)
    slug = models.SlugField(max_length=100, unique=True)
    likes = models.IntegerField()
    views = models.IntegerField()


    def __str__(self):
        return self.title



class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField()

