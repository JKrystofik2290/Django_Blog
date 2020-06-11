"""Models for database"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    """DB model for blog posts"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    time_posted = models.TimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'  # pylint: disable='no-member'

    def get_absolute_url(self):
        """Redirects to post details after a post is created"""
        return reverse('post-detail', kwargs={'pk': self.pk})
