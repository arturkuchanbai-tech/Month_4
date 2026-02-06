from django import forms
from .models import Proglang

class ProgLangForm(forms.ModelForm):
    class Meta:
        model = Proglang
        fields = '__all__'
