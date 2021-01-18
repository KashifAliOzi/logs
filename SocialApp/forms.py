from django.contrib.auth.forms import UserCreationForm
from .models import Users, BlogPost
from django.forms import ModelForm
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'image']
        # def __init__(self, *args, **kwargs):
        #     id = kwargs.pop('id')
        #     super(PostUpdateForm, self).__init__(*args, **kwargs)
        #     self.fields['id'].queryset = BlogPost.objects.filter(id=id)