from django.http import HttpResponse
from django.template import loader
from .models import Pokemon, EntrenadorPokemon   # ← usa el nombre actualizado del modelo
from pokedex.forms import PokemonForm, EntrenadorPokemonForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def index(request):
    pokemons = Pokemon.objects.all()
    entrenadores = EntrenadorPokemon.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'pokemons': pokemons, 'entrenadores': entrenadores}, request))


def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {'pokemon': pokemon}
    return HttpResponse(template.render(context, request))


def entrenador(request, entrenador_id):
    entrenador = EntrenadorPokemon.objects.get(id=entrenador_id)
    template = loader.get_template('display_entrenador.html')
    context = {'entrenador': entrenador}
    return HttpResponse(template.render(context, request))


@login_required
def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})


@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})


@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')


# 🔥 NUEVAS VISTAS PARA ENTRENADORES
@login_required
def add_entrenador(request):
    if request.method == "POST":
        form = EntrenadorPokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = EntrenadorPokemonForm()
    return render(request, 'trainer_form.html', {'form': form})


@login_required
def edit_entrenador(request, entrenador_id):
    entrenador = EntrenadorPokemon.objects.get(id=entrenador_id)
    if request.method == "POST":
        form = EntrenadorPokemonForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = EntrenadorPokemonForm(instance=entrenador)
    return render(request, 'trainer_form.html', {'form': form})


@login_required
def delete_entrenador(request, entrenador_id):
    entrenador = EntrenadorPokemon.objects.get(id=entrenador_id)
    entrenador.delete()
    return redirect('pokedex:index')


class CustomLoginView(LoginView):
    template_name = 'login_form.html'