from django.shortcuts import render
from .models import Servicio
from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    servicios= Servicio.objects.all()
    return render(request, 'home.html', {'servicios': servicios})
def locales(request):
    servicios= Servicio.objects.filter(tipo="local")
    return render(request, 'locales.html', {'servicios': servicios})

def musica(request):
    servicios= Servicio.objects.filter(tipo="musica")
    return render(request, 'musica.html', {'servicios': servicios})

def bebidas(request):
    servicios= Servicio.objects.filter(tipo="bebida")
    return render(request, 'bebidas.html', {'servicios': servicios})

def crearServicio(request):
    return render(request, 'crearServicioDu.html')

def detalle(request, nombre):
    servicio= Servicio.objects.get(nombre=nombre)
    return render(request, 'detalle.html', {'servicio': servicio})

def homeSinInicio(request):
    return render(request, 'home_sin_inicio.html')

def inicioSesion(request):
    return render(request, 'iniciar_sesion.html')

def reservas(request):
    return render(request, 'reservasDu.html')

def registrarMenu(request):
    return render(request, 'registrar.html')

def registrarCliente(request):
    return render(request, 'registroClien.html')

def registrarDuenio(request):
    return render(request, 'registroDu.html')