from django import forms
from .models import Animal, Especie

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'especie', 'data_nascimento', 'peso', 'data_de_cadastro',]
             