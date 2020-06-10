"""Models for Users database"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Database model for user profiles"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_user.jpg',
                              upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # pylint: disable='no-member'
