from rest_framework import viewsets
from pokedex.models import Pokemon, EntrenadorPokemon
from .serializers import PokemonSerializer, EntrenadorPokemonSerializer
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasScope
from rest_framework.permissions import IsAuthenticated, AllowAny


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    pagination_class = None

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]


class EntrenadorPokemonViewSet(viewsets.ModelViewSet):
    queryset = EntrenadorPokemon.objects.all()
    serializer_class = EntrenadorPokemonSerializer

    authentication_classes = [OAuth2Authentication]
    required_scopes = ['write']

    pagination_class = None

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), TokenHasScope()]
        return [AllowAny()]