from rest_framework import viewsets
from movies.models import Pelicula, Director
from .serializers import PeliculaSerializer, DirectorSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer