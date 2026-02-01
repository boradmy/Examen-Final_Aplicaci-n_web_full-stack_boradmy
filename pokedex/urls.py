from django.urls import path
from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.index, name="index"),

    # Pokémon
    path("<int:pokemon_id>/", views.pokemon, name="pokemon_directo"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),

    # Entrenadores
    path("entrenador/<int:entrenador_id>/", views.entrenador, name="entrenador"),
    path("add_entrenador/", views.add_entrenador, name="add_entrenador"),
    path("edit_entrenador/<int:entrenador_id>/", views.edit_entrenador, name="edit_entrenador"),
    path("delete_entrenador/<int:entrenador_id>/", views.delete_entrenador, name="delete_entrenador"),

    # Login
    path("login/", views.CustomLoginView.as_view(), name="login"),
]