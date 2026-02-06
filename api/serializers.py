from rest_framework import serializers
from movies.models import Pokemon, EntrenadorPokemon
from django.core.files.base import ContentFile
import base64

class PokemonSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Pokemon
        fields = '__all__'

    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'pokemon.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("La imagen no se encuentra con base64 válida.")
        return value


class EntrenadorPokemonSerializer(serializers.ModelSerializer):
    picture = serializers.CharField(required=False, allow_null=True)
    pokemons = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Pokemon.objects.all(),
        required=False
    )

    class Meta:
        model = EntrenadorPokemon
        fields = '__all__'

    def validate_picture(self, value):
        if value:
            try:
                format, imgstr = value.split(';base64,')
                ext = format.split('/')[-1]
                return ContentFile(
                    base64.b64decode(imgstr),
                    name=f'entrenador.{ext}'
                )
            except Exception:
                raise serializers.ValidationError("La imagen del entrenador no está en base64 válida.")
        return value