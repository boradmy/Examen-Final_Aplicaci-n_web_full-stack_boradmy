from django.contrib import admin
from .models import Pelicula, Director


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'anio')
    search_fields = ('titulo', 'genero')
    list_filter = ('genero', 'anio')
    ordering = ('titulo',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')
    list_filter = ('nacionalidad',)
    ordering = ('nombre',)
