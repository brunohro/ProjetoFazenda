from django.db import models

class Especie(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    peso = models.FloatField()
    data_de_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome