from django.db import models

# Create your models here.


class BlogPost(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    content = models.TextField()


class EmailSubscriber(models.Model):
    email = models.EmailField(max_length=100, unique=True)
