from django.db import models

# Create your models here.

class Anime(models.Model):
    nombre = models.CharField(max_length = 60)
    traduccion = models.CharField (max_length = 60)
    año = models.IntegerField()
    caps = models.IntegerField()
    creador = models.CharField(max_length = 60)
    site = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.nombre
    
class Pelicula(models.Model):
    nombre = models.CharField(max_length = 60)
    traduccion = models.CharField (max_length = 70)
    año = models.IntegerField()
    duracion = models.CharField(max_length = 30)
    creador = models.CharField(max_length = 60)
    site = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.nombre

class Videojuegos(models.Model):
    nombre = models.CharField(max_length = 60)
    traduccion = models.CharField (max_length = 60)
    año = models.IntegerField()
    plataforma = models.CharField(max_length = 60)
    creador = models.CharField(max_length = 60)
    
    def __str__(self):
        return self.nombre
    