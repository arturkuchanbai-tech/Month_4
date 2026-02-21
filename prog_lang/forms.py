from django import forms
<<<<<<< HEAD
from .models import ProgLang
=======
from prog_lang.models import ProgLang
>>>>>>> 88e1fbe6 (Классные работы)

class ProgLangForm(forms.ModelForm):
    class Meta:
        model = ProgLang
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"

        #если вдруг только определенные
        #fields = "title description".split()

        
>>>>>>> 88e1fbe6 (Классные работы)
