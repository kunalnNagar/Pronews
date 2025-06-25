from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Create UserName...'
        }
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Enter Your Email...'
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Create Password...'
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Confirm Password...'
        }
    ))

    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']