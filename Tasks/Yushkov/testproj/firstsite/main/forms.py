from django import forms
from .models import Coment


class AddComent(forms.Form):

    titel = forms.CharField(max_length=50, label = 'Titel')
    content = forms.CharField(widget=forms.Textarea, label = 'Content')
    issued = forms.DateTimeField()