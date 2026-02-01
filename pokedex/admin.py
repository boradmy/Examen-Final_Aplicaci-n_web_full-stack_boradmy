from django.contrib import admin
from .models import Pokemon, EntrenadorPokemon   

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(EntrenadorPokemon)
class EntrenadorPokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city', 'specialty')  # columnas visibles en el admin
    search_fields = ('name', 'city', 'specialty')        # barra de búsqueda
    list_filter = ('city', 'specialty')                  # filtros laterales