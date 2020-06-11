"""Configure forms for users app"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """Class for user registration"""
    email = forms.EmailField()

    class Meta:
        """Nested namespace for configurations"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """Class for updating user info"""
    email = forms.EmailField()

    class Meta:
        """Nested namespace for configurations"""
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """Class for updating user image"""
    class Meta:
        """Nested namespace for configurations"""
        model = Profile
        fields = ['image']
