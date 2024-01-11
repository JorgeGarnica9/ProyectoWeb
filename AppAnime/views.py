from django.shortcuts import render
from django.http import HttpResponse
from AppAnime.models import *
from AppAnime.forms import *

# Create your views here.

def incio(request):
    return render (request, 'AppAnime/inicio.html')


#Ver temas

def ver_anime(request):
    mis_anime = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'animes':mis_anime}
    return render(request, 'AppAnime/anime.html',info)

def ver_pelis(request):
    mis_pelis = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'pelis':mis_pelis}
    return render(request, 'AppAnime/peliculas.html',info)

def ver_juegos(request):
    mis_juegos = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'juegos':mis_juegos}
    return render(request, 'AppAnime/gaming.html',info)


#Agregar info a BBDD

def agregar_anime(request):
    
    if request.method == 'POST':
        new_form = AnimeFormulario(request.POST)
        
        if new_form.is_valid():
            info = new_form.cleaned_data
            
            new_anime = Anime(
                nombre=info['nombre'],
                traduccion=info['traduccion'],
                año=info['año'],
                caps=info['caps'],
                creador=info['creador'],
                site=info['site']
                )
            new_anime.save()

            return render(request, 'AppAnime/inicio.html')
        
    else: new_form = AnimeFormulario()
    
    return render(request, 'AppAnime/apiDjango_formAnime.html', {'mi_formu':new_form})

def agregar_pelicula(request):
    
    if request.method == 'POST':
        new_form = PeliculaFormulario(request.POST)
        
        if new_form.is_valid():
            info = new_form.cleaned_data
            
            new_peli = Pelicula(
                nombre=info['nombre'],
                traduccion=info['traduccion'],
                año=info['año'],
                duracion=info['duracion'],
                creador=info['creador'],
                site=info['site']
                )
            new_peli.save()

            return render(request, 'AppAnime/inicio.html')
        
    else: new_form = PeliculaFormulario()
    
    return render(request, 'AppAnime/apiDjango_formPeli.html', {'mi_formu2':new_form})


def agregar_videojuego(request):
    
    if request.method == 'POST':
        new_form = VideojuegoFormulario(request.POST)
        
        if new_form.is_valid():
            info = new_form.cleaned_data
            
            new_game = Videojuegos(
                nombre=info['nombre'],
                traduccion=info['traduccion'],
                año=info['año'],
                plataforma=info['plataforma'],
                creador=info['creador'],
                )
            new_game.save()

            return render(request, 'AppAnime/inicio.html')
        
    else: new_form = VideojuegoFormulario()
    
    return render(request, 'AppAnime/apiDjango_formGame.html', {'mi_formu3':new_form})


#Buscar info en BBDD

def buscar_anime(request):
    

    return render(request, 'AppAnime/buscarAnime.html')

def resultado_buscarAnime(request):
    
    if request.method == 'GET':
        
        nombre_pedido=request.GET['nombre']
        resultadosAnime = Anime.objects.filter(nombre__icontains=nombre_pedido)
        return render(request, 'AppAnime/buscarAnime.html', {'animes':resultadosAnime})
    
    else: return render(request, 'AppAnime/buscarAnime.html')
        
        
    
    