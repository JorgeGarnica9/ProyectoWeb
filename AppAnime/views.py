from django.shortcuts import render
from django.http import HttpResponse
from AppAnime.models import *

# Create your views here.
def ver_anime(request):
    mis_anime = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'animes':mis_anime}
    return render(request, 'AppAnime/anime.html',info)

def incio(request):
    return render (request, 'AppAnime/inicio.html')

def ver_pelis(request):
    mis_pelis = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'pelis':mis_pelis}
    return render(request, 'AppAnime/peliculas.html',info)

def ver_juegos(request):
    mis_juegos = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'juegos':mis_juegos}
    return render(request, 'AppAnime/gaming.html',info)



'''
def agregarAnime(request):
    anime1 = Anime(
        nombre = 'Dragon Ball',
        traduccion = 'Dragon Ball',
        año = 1986,
        caps = 153,
        creador = 'Akira Toriyama',
        site = 'Crunchyroll')
    anime1.save()
    
    return HttpResponse('Anime agregado correctamente...')

def agregarPelicula(request):
    pelicula = Pelicula(
        nombre = 'Dragon Ball Z: Chikyū Marugoto Chōkessen',
        traduccion = 'Dragon Ball Z: La batalla más grande del mundo está por comenzar',
        año = 1990,
        duracion = '60 minutos',
        creador = 'Akira Toriyama',
        site = 'Crunchyroll')
    pelicula.save()
    
    return HttpResponse('Pelicula agregada correctamente...')
    '''