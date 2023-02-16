from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class register_forms(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Confirmer mot de passe"}))
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class Login_forms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}))



    