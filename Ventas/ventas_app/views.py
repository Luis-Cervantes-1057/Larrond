from django.shortcuts import render
from .models import Ventas

# Create your views here.
def inicio_vista(request):
    
    ListadoVentas= Ventas.objects.all()
    return render(request, "gestionarVentas.html",{"lasventas" : ListadoVentas})