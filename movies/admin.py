from django.contrib import admin
from .models import Pokemon, EntrenadorPokemon


@admin.register(Pokemon)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'weight', 'height')
    search_fields = ('name', 'type')
    list_filter = ('type',)
    ordering = ('name',)


@admin.register(EntrenadorPokemon)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city', 'specialty')
    search_fields = ('name', 'city', 'specialty')
    list_filter = ('city', 'specialty')
    ordering = ('name',)