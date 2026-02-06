from django.db import models


class Pokemon(models.Model):
    # Usado como "Película" en la UI
    name = models.CharField(max_length=100, help_text="Título de la película")
    type = models.CharField(max_length=50, help_text="Género (Acción, Drama, Comedia, etc.)")
    height = models.FloatField(help_text="Año de estreno (ej. 2025)")
    weight = models.FloatField(help_text="Duración en minutos")
    picture = models.ImageField(upload_to='pokemons/', null=True, blank=True, help_text="Portada (opcional)")

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ("name",)

    def __str__(self):
        return self.name

    # Propiedades de conveniencia para plantillas (no obligatorias)
    @property
    def titulo(self):
        return self.name

    @property
    def genero(self):
        return self.type

    @property
    def anio(self):
        return int(self.height) if self.height is not None else None

    @property
    def duracion(self):
        return int(self.weight) if self.weight is not None else None


class EntrenadorPokemon(models.Model):
    # Usado como "Autor" en la UI
    name = models.CharField(max_length=100, help_text="Nombre del autor")
    age = models.IntegerField(help_text="Edad en años")
    city = models.CharField(max_length=100, blank=True, null=True, help_text="Ciudad (opcional)")
    specialty = models.CharField(max_length=50, blank=True, null=True, help_text="Especialidad (opcional)")
    picture = models.ImageField(upload_to='trainers/', null=True, blank=True, help_text="Foto (opcional)")
    pokemons = models.ManyToManyField(
        Pokemon,
        blank=True,
        related_name="autores",  # permite: pelicula.autores.all()
        help_text="Seleccione una o varias películas"
    )

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ("name",)

    def __str__(self):
        return self.name