"""Test_Blog django views handler"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost


def index(request):
    """Serves the index page of test_blog app"""
    context = {'posts': BlogPost.objects.all()}  # pylint: disable='no-member'
    return render(request, 'test_blog_index.html', context)


class PostListView(ListView):
    """Serves blog home view"""
    model = BlogPost
    template_name = 'test_blog_index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted', '-time_posted']


class PostDetailView(DetailView):
    """Serves individual blog post view"""
    model = BlogPost
    template_name = 'post_detail.html'


def about(request):
    """Serves the about page of test_blog app"""
    return render(request, 'test_blog_about.html',
                  {'title': 'About Test_Blog'})
