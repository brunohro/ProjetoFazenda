from django.contrib import admin
from .models import Animal, Especie

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'data_nascimento',)
    