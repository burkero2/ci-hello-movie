from django import forms
from .models import Item

class MovieForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'director', 'genre', 'summary', 'score', 'watched']