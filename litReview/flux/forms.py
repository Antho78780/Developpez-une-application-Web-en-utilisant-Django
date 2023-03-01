from django.forms import ModelForm
from django import forms
from account.models import User
from django.core.exceptions import ValidationError
from . import models

class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


class ReviewForm(ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline","rating", "body"]

class FollowingForm(forms.Form):
    username = forms.CharField(max_length=255)
    
    def clean(self):
        clean_data = super().clean()
        try:
            user = User.objects.get(username=self.cleaned_data["username"])
            clean_data["username"] = user
        except (User.DoesNotExist, ValueError):
            clean_data["username"] = None
            raise ValidationError("L'utilisateur n'existe pas")
        return clean_data

class UnsubscribeForm(forms.Form):
    user_id = forms.CharField(widget=forms.HiddenInput())
    
