from django.db import models
from django.urls import reverse

# Create your models here.

class Juego(models.Model):
    id_juego=models.CharField(primary_key=True, max_length=5)
    nombre=models.CharField(max_length=20)
    genero=models.CharField(max_length=15)
    annio_publicacion = models.DateField(null=True, blank=True)
    descripcion=models.TextField(max_length=1000)


    def __str__(self):
        return self.nombre

