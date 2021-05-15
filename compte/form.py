from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput,EmailInput,PasswordInput


class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'user name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ex: email@hmail.com'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'choose a password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'entrer password again'})

        }
