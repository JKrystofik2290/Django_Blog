"""Test_Blog django views handler"""
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Serves the user registration page"""
    form = UserCreationForm()
    return render(request, 'user_reg.html', {'form': form})
