"""Test Blog URLs"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='test_blog-home'),
    path('about/', views.about, name='test_blog-about'),
]
