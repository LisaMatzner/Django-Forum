from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.
class ThreadStatus(models.TextChoices):
    DEFAULT = "default", "Normal"
    CLOSED = "closed", "Closed"
    PINNED = "pinned", "Pinned"
    NEW = "new", "New"


class Thread(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_opened_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    flag = models.CharField(choices=ThreadStatus.choices, max_length=20, default=ThreadStatus.NEW)
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


    def save(self, *args, **kwargs):
        if not self.pk:
            self.author.number_of_posts += 1
            self.author.save()

        return super().save(*args, **kwargs)
    

    def like_count(self):
        return self.likes.count()  # Count all likes for this comment
    

    def __str__(self):
        return f'Comment by {self.author} on {self.thread}'
    

class Like(models.Model):

    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')


    class Meta:
        unique_together = ('liked_by', 'comment')  # Enforce one like per user per comment



    def __str__(self):
        return f'{self.comment} was liked by {self.liked_by}'

