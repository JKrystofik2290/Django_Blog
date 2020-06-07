"""Models for database"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """DB model for blog posts"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # need to change to user timezone
    date_posted = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()
