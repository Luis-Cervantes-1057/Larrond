from django.shortcuts import render
from .models import Empleados
# Create your views here.

def inicio_vista(request):
    #obtener todos los registros de la tabla Materia
    ListadoEmpleados= Empleados.objects.all()
    return render(request, "gestionarEmpleados.html",{"losempleados" : ListadoEmpleados})