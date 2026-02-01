from django import forms
from .models import Pokemon, EntrenadorPokemon


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'  # Incluye todos los campos del modelo Pokemon
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'height': 'Altura',
            'weight': 'Peso',
            'picture': 'Imagen',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }


class EntrenadorPokemonForm(forms.ModelForm):
    class Meta:
        model = EntrenadorPokemon
        fields = '__all__'  # Incluye todos los campos del modelo EntrenadorPokemon
        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'city': 'Ciudad',
            'specialty': 'Especialidad',
            'picture': 'Imagen',
            'pokemons': 'Pokémons',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pokemons': forms.CheckboxSelectMultiple(),  # lista de checkboxes para elegir varios Pokémon
        }