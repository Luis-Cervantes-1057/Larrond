from django.shortcuts import render
from .models import Proveedor

# Create your views here.
def inicio_vista(request):
    #obtener todos los registros de la tabla Materia
    ListadoProveedor= Proveedor.objects.all()
    return render(request, "gestionarProveedor.html",{"losprov" : ListadoProveedor})