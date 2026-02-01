from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet, EntrenadorPokemonViewSet

router = DefaultRouter()
router.register(r'pokemons', PokemonViewSet, basename='pokemon')
router.register(r'entrenadores', EntrenadorPokemonViewSet, basename='entrenador')

urlpatterns = [
    path('', include(router.urls)),
]