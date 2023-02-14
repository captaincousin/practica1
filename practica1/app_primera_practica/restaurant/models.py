from django.db import models
# Create your models here.

from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def _str_(self):
        return self.nombre

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    trabajador = models.ForeignKey('Trabajador', on_delete=models.SET_NULL, null=True, blank=True)

    def _str_(self):
        return self.nombre

class Trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)

    def _str_(self):
        return self.nombre