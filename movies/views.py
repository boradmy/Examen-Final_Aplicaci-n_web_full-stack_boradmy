from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render

from .models import Pelicula, Director
from .forms import PeliculaForm, DirectorForm


# ---------- Vistas principales ----------
def index(request):
    """
    Página principal:
      - Lista de Películas
      - Lista de Directores
    """
    peliculas = Pelicula.objects.all().order_by('titulo')
    directores = Director.objects.all().order_by('nombre')
    return render(request, 'index.html', {
        'peliculas': peliculas,
        'directores': directores,
    })


def pelicula(request, id):
    """
    Detalle de una película
    """
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'display_peliculas.html', {
        'pelicula': pelicula
    })


def director(request, id):
    """
    Detalle de un director
    """
    director = get_object_or_404(Director, id=id)
    return render(request, 'display_autores.html', {
        'director': director
    })


# ---------- Películas (CRUD) ----------
@login_required
def add_pelicula(request):
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Película creada correctamente.")
            return redirect('movies:index')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas_form.html', {'form': form})


@login_required
def edit_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    if request.method == "POST":
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, "Película actualizada correctamente.")
            return redirect('movies:index')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'peliculas_form.html', {'form': form})


@login_required
def delete_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    pelicula.delete()
    messages.success(request, "Película eliminada correctamente.")
    return redirect('movies:index')


# ---------- Directores (CRUD) ----------
@login_required
def add_director(request):
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Director creado correctamente.")
            return redirect('movies:index')
    else:
        form = DirectorForm()
    return render(request, 'autores_form.html', {'form': form})


@login_required
def edit_director(request, id):
    director = get_object_or_404(Director, id=id)
    if request.method == "POST":
        form = DirectorForm(request.POST, request.FILES, instance=director)
        if form.is_valid():
            form.save()
            messages.success(request, "Director actualizado correctamente.")
            return redirect('movies:index')
    else:
        form = DirectorForm(instance=director)
    return render(request, 'autores_form.html', {'form': form})


@login_required
def delete_director(request, id):
    director = get_object_or_404(Director, id=id)
    director.delete()
    messages.success(request, "Director eliminado correctamente.")
    return redirect('movies:index')


# ---------- Login / Logout ----------
class CustomLoginView(LoginView):
    template_name = 'login_form.html'


class CustomLogoutView(LogoutView):
    next_page = 'movies:index'
