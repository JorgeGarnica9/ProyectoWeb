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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', incio, name='Inicio'),
    
    #URL'S usuarios
    path('login/', iniciar_sesion),
    path('signup/', registro),
    path('logout/', cerrar_sesion),
    path('edit/', editar_perfil),
    path('agregarImagen/', agregarImagen, name= 'Subir Avatar'),
    
    
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
    path('buscarPeli/', buscar_peli),
    path('buscarJuego/', buscar_juego),
    path('resultados/', resultado_buscarAnime),
    path('resultadosPeli/', resultado_buscarPeli),
    path('resultadosJuego/', resultado_buscarJuego),
    
    #URL'S actualización de datos
    path('updateAnime/<id_anime>', actualizar_anime, name='editarAnime'),
    path('updateJuego/<id_juego>', actualizar_juego, name='editarJuego'),
    path('updatePeli/<id_peli>', actualizar_peli, name='editarPeli'),
    
    #URL'S eliminación de datos
    path('borrarAnime/<id_anime>', eliminar_anime, name = 'eliminarAnime'),
    path('borrarJuego/<id_juego>', eliminar_juego, name='eliminarJuego'),
    path('borrarPeli/<id_peli>', eliminar_peli, name='eliminarPeli'),
    
    #URL'S del creador
    path('acerca/', acerca_de),
    path('contacto/', contacto),
    path('terminos/', terminos),
    
    #URL'S de listados para edit/erase
    path('editAnime/', editAnime),
    path('eraseAnime/', eraseAnime),
    path('editPeli/', editPeli),
    path('erasePeli/', erasePeli),
    path('editJuego/', editJuego),
    path('eraseJuego/', eraseJuego),
    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)