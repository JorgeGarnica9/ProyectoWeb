"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppAnime.views import *
from AppAnime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', incio, name='Inicio'),
    
    #URL'S modelos
    path('verAnime/', ver_anime, name='Animes'),
    path('verPelis/', ver_pelis, name='Peliculas'),
    path('verJuegos/', ver_juegos, name='Juegos'),
    
    #URL'S creación de datos
    path('nuevoAnime/', agregar_anime),
    path('nuevaPeli/', agregar_pelicula),
    path('nuevoJuego/', agregar_videojuego), 

    #URL'S búsqueda de datos
    path('buscarAnime/', buscar_anime),
    path('resultados/', resultado_buscarAnime),
]