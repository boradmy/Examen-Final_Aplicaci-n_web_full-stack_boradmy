from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),

    # Películas
    path("pelicula/<int:id>/", views.pelicula, name="pelicula"),
    path("pelicula/add/", views.add_pelicula, name="add_pelicula"),
    path("pelicula/<int:id>/edit/", views.edit_pelicula, name="edit_pelicula"),
    path("pelicula/<int:id>/delete/", views.delete_pelicula, name="delete_pelicula"),

    # Autores
    path("autor/<int:id>/", views.autor, name="autor"),
    path("autor/add/", views.add_autor, name="add_autor"),
    path("autor/<int:id>/edit/", views.edit_autor, name="edit_autor"),
    path("autor/<int:id>/delete/", views.delete_autor, name="delete_autor"),

    # Login
    path("login/", views.CustomLoginView.as_view(), name="login"),
]