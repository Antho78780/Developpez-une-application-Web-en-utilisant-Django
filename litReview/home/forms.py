from django import forms

class TicketForm(forms.Form):
    titre = forms.CharField(label="Titre")
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':0, 'cols':0}))
    image = forms.ImageField()

class ReviewForm(forms.Form):
    titre = forms.CharField(label="Titre")
    commentaire = forms.CharField(label="Commentaire", max_length=1000)

class FollowForm(forms.Form):
   username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
