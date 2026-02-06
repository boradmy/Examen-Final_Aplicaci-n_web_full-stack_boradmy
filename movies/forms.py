from django import forms
from .models import Pokemon, EntrenadorPokemon


class PeliculaForm(forms.ModelForm):
    """
    Form para el modelo Pokemon, usado como 'Película' en la UI.
    """
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Título',
            'type': 'Género',
            'height': 'Año',       # reutilizamos height como 'Año'
            'weight': 'Duración',  # reutilizamos weight como 'Duración'
            'picture': 'Portada',
        }
        help_texts = {
            'name': 'Ingresa el título de la película.',
            'type': 'Ejemplo: Acción, Drama, Comedia...',
            'height': 'Año de estreno (por ejemplo: 2024).',
            'weight': 'Duración en minutos (por ejemplo: 120).',
            'picture': 'Imagen de portada (opcional).',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título de la película',
                'autocomplete': 'off',
            }),
            'type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Género',
                'autocomplete': 'off',
            }),
            # Año (antes height). Si tu campo es FloatField, permitimos decimales, pero sugiere año entero.
            'height': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Año (ej. 2025)',
                'step': '1',
                'min': '1888',  # primer año de películas
                'max': '2100',
            }),
            # Duración en minutos (antes weight).
            'weight': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración (min)',
                'step': '1',
                'min': '1',
                'max': '1000',
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class AutorForm(forms.ModelForm):
    """
    Form para el modelo EntrenadorPokemon, usado como 'Autor' en la UI.
    """
    class Meta:
        model = EntrenadorPokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'city': 'Ciudad',
            'specialty': 'Especialidad',
            'picture': 'Foto',
            'pokemons': 'Películas',  # relación con 'Pokemon' (Películas)
        }
        help_texts = {
            'name': 'Nombre y apellido del autor.',
            'age': 'Edad del autor en años.',
            'city': 'Ciudad de residencia.',
            'specialty': 'Área de especialidad (guion, dirección, etc.).',
            'picture': 'Fotografía del autor (opcional).',
            'pokemons': 'Selecciona una o varias películas asociadas.',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del autor',
                'autocomplete': 'off',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'min': '0',
                'max': '120',
                'step': '1',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad',
                'autocomplete': 'off',
            }),
            'specialty': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Especialidad (dirección, guion, fotografía, ...)',
                'autocomplete': 'off',
            }),
            'picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            # ManyToMany con 'Pokemon' (Películas) como checkboxes
            'pokemons': forms.CheckboxSelectMultiple(),
        }

    # Si quieres forzar orden alfabético de las películas en el widget:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'pokemons' in self.fields:
            self.fields['pokemons'].queryset = Pokemon.objects.all().order_by('name')