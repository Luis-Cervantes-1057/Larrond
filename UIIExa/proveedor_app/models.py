from django.db import models

# Create your models here.

class Proveedor (models.Model):
    id_proveedor = models.SmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    c_electronico = models.CharField(max_length=25)
    stock = models.CharField(max_length=10)
    fecha_ult_entrega = models.DateField()
    
    def __str__(self):
        return self.nombre