from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.

class Thread(models.Model):
    FLAG_CHOICES = [("d", "default"), ("c","closed"), ("s" ,"sticky"), ("n" ,"new")]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_opened_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    flag = models.CharField(choices=FLAG_CHOICES, max_length=20, default=FLAG_CHOICES[3])
    slug = models.SlugField(max_length=100, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        if not Thread.objects.filter(slug=base_slug).exists():
            self.slug = base_slug
        else:
            counter = 1
            new_slug = f"{base_slug}-{counter}"
            while Thread.objects.filter(slug=new_slug).exists():
                counter += 1
                new_slug = f"{base_slug}-{counter}"
            self.slug = new_slug

        return super().save(*args, **kwargs)



class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.author.number_of_posts += 1
            self.author.save()

        return super().save(*args, **kwargs)

