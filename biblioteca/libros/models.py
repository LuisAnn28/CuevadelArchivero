from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    anio = models.IntegerField("Año")
    genero = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"