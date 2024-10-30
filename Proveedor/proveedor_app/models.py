from django.db import models

# Create your models here.

class Proveedor (models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    num_ruta = models.PositiveSmallIntegerField()
    cant_prod = models.IntegerField()
    peso = models.FloatField()
    id_empleado = models.IntegerField()
    tipo_prod = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_prod