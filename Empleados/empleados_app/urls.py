from django.urls import path, include
from empleados_app import views

urlpatterns = [
    path("", views.inicio_vista, name="views.inicio_vista")
]