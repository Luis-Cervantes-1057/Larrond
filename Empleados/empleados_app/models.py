from django.db import models

# Create your models here.

class Empleados (models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=20)
    rfc = models.CharField(max_length=12)
    curp = models.CharField(max_length=12)
    num_celular = models.IntegerField()
    direccion = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre