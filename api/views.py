from rest_framework import viewsets
from movies.models import Pelicula
from .serializers import PeliculaSerializer


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
