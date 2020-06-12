"""Models for Users database"""
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Database model for user profiles"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_user.jpg',
                              upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  # pylint: disable='no-member'

    # def save(self, *args, **kwargs):
    #     """Overwritting parent save method"""
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)  # pylint: disable='no-member'

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)  # pylint: disable='no-member'
