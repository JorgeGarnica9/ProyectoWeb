from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppAnime.models import *

class AnimeFormulario(forms.Form):
    nombre = forms.CharField(max_length = 60)
    traduccion = forms.CharField (max_length = 60)
    año = forms.IntegerField()
    caps = forms.IntegerField()
    creador = forms.CharField(max_length = 60)
    site = forms.CharField(max_length = 60)
        
class PeliculaFormulario(forms.Form):
    nombre = forms.CharField(max_length = 60)
    traduccion = forms.CharField (max_length = 70)
    año = forms.IntegerField()
    duracion = forms.CharField(max_length = 30)
    creador = forms.CharField(max_length = 60)
    site = forms.CharField(max_length = 60)
    
class VideojuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length = 60)
    traduccion = forms.CharField (max_length = 60)
    año = forms.IntegerField()
    plataforma = forms.CharField(max_length = 60)
    creador = forms.CharField(max_length = 60)
    
class RegistrarUsuario(UserCreationForm):
    username = forms.CharField(max_length=20, label='Nombre de usuario')
    first_name = forms.CharField(max_length=20, label='Nombre')
    last_name = forms.CharField(max_length=40, label='Apellido')
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, max_length=15, label='Ingrese su contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, max_length=15, label='Repita su contraseña', widget=forms.PasswordInput)
        
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    
class EditarUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Ingrese su nombre')
    last_name = forms.CharField(max_length=40, label='Ingrese su apellido')
    email = forms.EmailField()
    password1 = forms.CharField(min_length=8, max_length=15, label='Ingrese su contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, max_length=15, label='Repita su contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        
        model = AvatarImagen
        fields =  ['imagen']