"""Adds access on admin page"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
