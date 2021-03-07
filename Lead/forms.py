from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class Register(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']