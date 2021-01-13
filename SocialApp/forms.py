from django.contrib.auth.forms import UserCreationForm
from .models import Users
from django.forms import ModelForm
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']
