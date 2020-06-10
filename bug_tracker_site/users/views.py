"""Test_Blog django views handler"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    """Serves the user registration page"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('test_blog-home')

    else:
        form = UserRegisterForm()

    return render(request, 'user_reg.html', {'form': form})


@login_required
def profile(request):
    """Serves the users profile page"""
    return render(request, 'profile.html')
