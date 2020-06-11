"""Registers app models with site admin page."""
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
