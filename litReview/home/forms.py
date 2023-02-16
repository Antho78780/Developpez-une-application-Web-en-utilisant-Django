from django.forms import ModelForm

from . import models

class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


# # class ReviewForm(ModelForm):
# #     titre = forms.CharField(label="Titre")
# #     commentaire = forms.CharField(label="Commentaire", max_length=1000)

