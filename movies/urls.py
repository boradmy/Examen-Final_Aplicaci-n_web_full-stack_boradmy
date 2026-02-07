from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),

    # Películas
    path('pelicula/<int:id>/', views.pelicula, name='pelicula'),
    path('pelicula/add/', views.add_pelicula, name='add_pelicula'),
    path('pelicula/edit/<int:id>/', views.edit_pelicula, name='edit_pelicula'),
    path('pelicula/delete/<int:id>/', views.delete_pelicula, name='delete_pelicula'),

    # Directores
    path('director/<int:id>/', views.director, name='director'),
    path('director/add/', views.add_director, name='add_director'),
    path('director/edit/<int:id>/', views.edit_director, name='edit_director'),
    path('director/delete/<int:id>/', views.delete_director, name='delete_director'),

    # Login / Logout
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
