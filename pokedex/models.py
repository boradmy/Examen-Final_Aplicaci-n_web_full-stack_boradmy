from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    picture = models.ImageField(upload_to='pokemons/', null=True, blank=True)

    def __str__(self):
        return self.name


class EntrenadorPokemon(models.Model):   # ← nombre corregido
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100, blank=True, null=True)   # opcional
    specialty = models.CharField(max_length=50, blank=True, null=True)  # opcional
    picture = models.ImageField(upload_to='trainers/', null=True, blank=True)  # avatar opcional
    pokemons = models.ManyToManyField(Pokemon, blank=True)

    def __str__(self):
        return self.name