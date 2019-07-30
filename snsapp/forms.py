from django import forms
from .models import Sns

class NewSns(forms.ModelForm):
    class Meta:
        model = Sns
        fields = ['title', 'date', 'body', 'img']