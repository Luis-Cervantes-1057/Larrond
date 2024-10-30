from django.shortcuts import render
from .models import Clientes

# Create your views here.
def inicio_vista (request):
    
    ListadoClientes = Clientes.objects.all()
    return render(request, "gestionarClientes.html",{"losclientes" : ListadoClientes})