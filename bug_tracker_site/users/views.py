"""Test_Blog django views handler"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    """Serves the user registration page"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('test_blog-home')

    else:
        form = UserRegisterForm()

    return render(request, 'user_reg.html', {'form': form})


def profile(request):
    """Serves the users profile page"""
    return render(request, 'profile.html')