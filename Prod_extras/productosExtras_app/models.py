from django.db import models

# Create your models here.

class ProductosExtras (models.Model):
    id_prod = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    tipo = models.CharField(max_length=10)
    talla = models.CharField(max_length=5)
    peso = models.FloatField()
    precio_uni = models.FloatField()
    id_proveedor = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nombre