"""Models for database"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """DB model for blog posts"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    time_posted = models.TimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()
