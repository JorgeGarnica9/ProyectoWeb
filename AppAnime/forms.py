from django import forms    

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