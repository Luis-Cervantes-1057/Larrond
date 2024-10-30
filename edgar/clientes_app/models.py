from django.db import models

# Create your models here.

class Clientes (models.Model):
    id_clientes = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=12)
    
    def __str__(self):
        return self.nombre
    