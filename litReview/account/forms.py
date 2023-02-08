from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Login_forms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))

class register_forms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    