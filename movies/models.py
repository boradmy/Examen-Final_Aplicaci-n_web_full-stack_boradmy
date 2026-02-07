from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='directores/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    anio = models.IntegerField()
    picture = models.ImageField(upload_to='peliculas/', blank=True, null=True)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='peliculas'
    )

    def __str__(self):
        return self.titulo
