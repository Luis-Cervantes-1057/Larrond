from django.db import models

# Create your models here.

class Clientes (models.Model):
    Id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    num_celular = models.IntegerField()
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre 