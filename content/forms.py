from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Entry


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'text']

    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.text = self.cleaned_data['text']

        if commit:
            blog_post.save()
        return blog_post
