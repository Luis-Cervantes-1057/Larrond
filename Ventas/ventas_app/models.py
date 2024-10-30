from django.db import models

# Create your models here.
class Ventas (models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_producto = models.IntegerField()
    cliente = models.CharField(max_length=15)
    cantidad = models.IntegerField()
    precio = models.CharField(max_length=10)
    gramos = models.FloatField()
    servicios = models.CharField(max_length=15)
    id_empleado = models.IntegerField()

    def __str__(self):
        return self.cliente