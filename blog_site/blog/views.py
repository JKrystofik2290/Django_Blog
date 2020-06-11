"""Blog django views handler"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,
                                  DeleteView)
from .models import BlogPost

# was replaced with class bassed view "PostListView"
# def index(request):
#     """Serves the index page of blog app"""
#     context = {'posts': BlogPost.objects.all()}  # pylint: disable='no-member'
#     return render(request, 'blog_index.html', context)


class PostListView(ListView):
    """Serves blog home view"""
    model = BlogPost
    template_name = 'blog_index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted', '-time_posted']
    paginate_by = 5


class UserPostListView(ListView):
    """Serves users blogs view"""
    model = BlogPost
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return BlogPost.objects.filter(author=user).order_by(
            '-date_posted', '-time_posted')


class PostDetailView(DetailView):
    """Serves individual blog post view"""
    model = BlogPost
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    """Serves view to create a blog post"""
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Serves view to Update a blog post"""
    model = BlogPost
    fields = ['title', 'content']
    template_name = 'post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Serves view to delete a blog post"""
    model = BlogPost
    template_name = 'post_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    """Serves the about page of blog app"""
    return render(request, 'blog_about.html', {'title': 'About Blog'})
