from django.db import models

# Create your models here.
class Meseros(models.Model):
    nombre = models.CharField(max_length=50,default='')
    pais = models.CharField(max_length=60,default='')
    edad = models.IntegerField(default=18)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"