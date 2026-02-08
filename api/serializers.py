from rest_framework import serializers
from movies.models import Pelicula, Director

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"