
from AppAnime.models import *
from AppAnime.forms import *

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def incio(request):
    return render (request, 'AppAnime/inicio.html')

#----------------------------------------------------------------------------------------   
#                            USERS: REGISTER/LOGIN/LOGOUT/EDIT
#----------------------------------------------------------------------------------------   

def iniciar_sesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data = request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data
            
            usuario = info['username']
            contra = info['password']
            
            usuario_actual = authenticate(username = usuario, password = contra)
            
            if usuario_actual is not None:
                login(request, usuario_actual)
                
                return render(request, 'AppAnime/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            
        else: 
            
            return render(request, 'AppAnime/inicio.html', {'mensaje':'Error, datos incorrectos!!'})
        
    else:
        formulario = AuthenticationForm()     
    return render(request, 'Registro/login.html', {'formu':formulario})


def registro(request):
    
    if request.method == 'POST':
        
        formulario = RegistrarUsuario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data

            usuario = info ['username']
            
            formulario.save()
            
            return render(request, 'AppAnime/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
    else:
        formulario = RegistrarUsuario()
        
    return render(request, 'Registro/registrarUsuario.html', {'formu':formulario})


def cerrar_sesion(request):
    logout(request)
    
    return render(request, 'Registro/logout.html')

def editar_perfil(request):
    
    usuario_actual = request.user
    
    if request.method == 'POST':
    
        formulario = EditarUsuario(request.POST)
    
        if formulario.is_valid():
        
            info = formulario.cleaned_data

            usuario_actual.first_name = info ['first_name']
            usuario_actual.last_name = info ['last_name']
            usuario_actual.email = info ['email']
            
            usuario_actual.save()
            
            return render(request, 'AppAnime/inicio.html', {'mensaje':'Datos de usuario actualizados'})
    else:
        formulario = EditarUsuario(initial={
            'first_name':usuario_actual.first_name,
            'last_name':usuario_actual.last_name,
            'email':usuario_actual.email,
            
        })
    
    return render(request, 'Registro/editarUsuario.html', {'formu':formulario})


#----------------------------------------------------------------------------------------   
#                                 VISTAS PRINCIPALES
#----------------------------------------------------------------------------------------   

def ver_anime(request):
    mis_anime = Anime.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'animes':mis_anime}
    return render(request, 'AppAnime/anime.html',info)

def ver_pelis(request):
    mis_pelis = Pelicula.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'pelis':mis_pelis}
    return render(request, 'AppAnime/peliculas.html',info)

def ver_juegos(request):
    mis_juegos = Videojuegos.objects.all() #obtiene todos los datos de mi tabla Anime
    info = {'juegos':mis_juegos}
    return render(request, 'AppAnime/gaming.html',info)

#----------------------------------------------------------------------------------------   
#                            Crear info en BBDD
#----------------------------------------------------------------------------------------   

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

@login_required
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

#----------------------------------------------------------------------------------------   
#                            Buscar info en BBDD
#----------------------------------------------------------------------------------------   

def buscar_anime(request):

    return render(request, 'AppAnime/buscarAnime.html')

def resultado_buscarAnime(request):
    
    if request.method == 'GET':
        
        nombre_pedido=request.GET['nombre']
        resultadosAnime = Anime.objects.filter(nombre__icontains=nombre_pedido)
        return render(request, 'AppAnime/buscarAnime.html', {'animes':resultadosAnime})
    
    else: return render(request, 'AppAnime/buscarAnime.html')
        
        
def buscar_peli(request):

    return render(request, 'AppAnime/buscarPeli.html')

def resultado_buscarPeli(request):
    
    if request.method == 'GET':
        
        nombre_pedido=request.GET['nombre']
        resultadosPeli = Pelicula.objects.filter(nombre__icontains=nombre_pedido)
        return render(request, 'AppAnime/buscarPeli.html', {'pelis':resultadosPeli})
    
    else: return render(request, 'AppAnime/buscarPeli.html')    
    

def buscar_juego(request):

    return render(request, 'AppAnime/buscarJuego.html')

def resultado_buscarJuego(request):
    
    if request.method == 'GET':
        
        nombre_pedido=request.GET['nombre']
        resultadosJuego = Videojuegos.objects.filter(nombre__icontains=nombre_pedido)
        return render(request, 'AppAnime/buscarJuego.html', {'juegos':resultadosJuego})
    
    else: return render(request, 'AppAnime/buscarJuego.html')    

#----------------------------------------------------------------------------------------   
#                            Actualizar info en BBDD
#----------------------------------------------------------------------------------------   

def actualizar_anime(request, nombre_anime):
    
    anime_elegido = Anime.objects.get(nombre=nombre_anime)
    
    if request.method == 'POST':
        new_form = AnimeFormulario(request.POST)
        
        if new_form.is_valid():
            info = new_form.cleaned_data
            
            anime_elegido.nombre=info['nombre']
            anime_elegido.traduccion=info['traduccion']
            anime_elegido.año=info['año']
            anime_elegido.caps=info['caps']
            anime_elegido.creador=info['creador']
            anime_elegido.site=info['site']
                
            anime_elegido.save()

            return render(request, 'AppAnime/inicio.html')
        
    else: new_form = AnimeFormulario(initial={
        'nombre':anime_elegido.nombre,
        'traduccion':anime_elegido.traduccion,
        'año':anime_elegido.año,
        'caps':anime_elegido.caps,
        'creador':anime_elegido.creador,
        'site':anime_elegido.site})
    
    return render(request, 'AppAnime/updateAnime.html', {'mi_formu':new_form})


def actualizar_juego(request, nombre_juego):
    
    juego_elegido = Videojuegos.objects.get(nombre=nombre_juego)
    
    if request.method == 'POST':
        new_form = VideojuegoFormulario(request.POST)
        
        if new_form.is_valid():
            info = new_form.cleaned_data
            
            juego_elegido.nombre=info['nombre']
            juego_elegido.traduccion=info['traduccion']
            juego_elegido.año=info['año']
            juego_elegido.plataforma=info['plataforma']
            juego_elegido.creador=info['creador']
                
            juego_elegido.save()

            return render(request, 'AppAnime/inicio.html')
        
    else: new_form = VideojuegoFormulario(initial={
        'nombre':juego_elegido.nombre,
        'traduccion':juego_elegido.traduccion,
        'año':juego_elegido.año,
        'plataforma':juego_elegido.plataforma,
        'creador':juego_elegido.creador})
    
    return render(request, 'AppAnime/updateJuego.html', {'mi_formu':new_form})

def actualizar_peli(request, nombre_peli):
    
    peli_elegida = Pelicula.objects.get(nombre=nombre_peli)
    
    if request.method == 'POST':
        new_form = PeliculaFormulario(request.POST)
        
        if new_form.is_valid():
            info = new_form.cleaned_data
            
            peli_elegida.nombre=info['nombre']
            peli_elegida.traduccion=info['traduccion']
            peli_elegida.año=info['año']
            peli_elegida.duracion=info['duracion']
            peli_elegida.creador=info['creador']
            peli_elegida.site=info['site']
                
            peli_elegida.save()

            return render(request, 'AppAnime/inicio.html')
        
    else: new_form = PeliculaFormulario(initial={
        'nombre':peli_elegida.nombre,
        'traduccion':peli_elegida.traduccion,
        'año':peli_elegida.año,
        'duracion':peli_elegida.duracion,
        'creador':peli_elegida.creador,
        'site':peli_elegida.site})
    
    return render(request, 'AppAnime/updatePeli.html', {'mi_formu':new_form})

#----------------------------------------------------------------------------------------   
#                            Borrar info en BBDD
#----------------------------------------------------------------------------------------   

def eliminar_anime(request, nombre_anime):
    anime_elegido = Anime.objects.get(nombre=nombre_anime)
    anime_elegido.delete()
    
    return render(request, 'AppAnime/anime.html')

def eliminar_juego(request, nombre_juego):
    juego_elegido = Videojuegos.objects.get(nombre=nombre_juego)
    juego_elegido.delete()
    
    return render(request, 'AppAnime/gaming.html')

def eliminar_peli(request, nombre_peli):
    peli_elegida = Pelicula.objects.get(nombre=nombre_peli)
    peli_elegida.delete()
    
    return render(request, 'AppAnime/peliculas.html')