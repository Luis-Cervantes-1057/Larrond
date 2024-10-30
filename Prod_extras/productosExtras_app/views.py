from django.shortcuts import render
from .models import ProductosExtras

# Create your views here.
def inicio_vista(request):

    ListadoProdExtras= ProductosExtras.objects.all()
    return render(request, "gestionarProdExtras.html",{"losextras" : ListadoProdExtras})