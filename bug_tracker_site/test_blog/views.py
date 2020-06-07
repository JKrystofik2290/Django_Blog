"""Test_Blog django views handler"""
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost


def index(request):
    """Serves the index page of test_blog app"""
    context = {'posts': BlogPost.objects.all()}  # pylint: disable='no-member'
    return HttpResponse(render(request, 'test_blog_index.html', context))


def about(request):
    """Serves the about page of test_blog app"""
    return HttpResponse(
        render(request, 'test_blog_about.html', {'title': 'About Test_Blog'}))
