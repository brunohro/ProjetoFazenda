from django.shortcuts import render
from .models import Animal, Especie

def index(request):
    animais = Animal.objects.all()
    especies = Especie.objects.all()
    return render(request, 'index.html', {'animais': animais, 'especies': especies})

