"""Test_Blog django views handler"""
from django.shortcuts import render
from django.http import HttpResponse

posts = [{
    'author': 'JoeK',
    'title': 'My First Post',
    'content': 'Some stuff to blog about.',
    'date_posted': '6/5/2020 3:30pm'
}, {
    'author': 'MattK',
    'title': "Matt's Blog Post",
    'content': 'Matt likes to cook!',
    'date_posted': '6/6/2020 10:23am'
}]


def index(request):
    """Serves the index page of test_blog app"""
    context = {'posts': posts}
    return HttpResponse(render(request, 'test_blog/index.html', context))


def about(request):
    """Serves the about page of test_blog app"""
    return HttpResponse(
        render(request, 'test_blog/about.html', {'title': 'About Test_Blog'}))
