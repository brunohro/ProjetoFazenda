from django.shortcuts import render, redirect
from .models import Animal, Especie
from .forms import AnimalForm

def index(request):
    animais = Animal.objects.all()
    especies = Especie.objects.all()
    return render(request, 'index.html', {'animais': animais, 'especies': especies})

def listar_animais(request):
    animais = Animal.objects.all()
    especies = Especie.objects.all()
    return render(request, 'animais/listar_animais.html', {'animais': animais, 'especies': especies})

def cadastrar_animais(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_animais')
        
    else:
        form = AnimalForm()
    return render(request, 'animais/cadastrar_animais.html', {'form': form})

def editar_animais(request, id):
    animal = Animal.objects.get(id=id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('listar_animais')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animais/editar_animais.html', {'form': form})

def remover_animal(request, id):
    animal = Animal.objects.get(id=id)
    animal.delete()
    return redirect('listar_animais')