from django.shortcuts import render
from .models import Proveedor

# Create your views here.
def inicio_vista(request):
    
    ListadoProveedor= Proveedor.objects.all()
    return render(request, "gestionarMuebleria.html",{"losprov" : ListadoProveedor})