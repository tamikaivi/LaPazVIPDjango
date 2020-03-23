from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def crearServicio(request):
    return render(request, 'crearServicioDu.html')

def detalle(request):
    return render(request, 'detalle.html')

def homeSinInicio(request):
    return render(request, 'home_sin_inicio.html')

def inicioSesion(request):
    return render(request, 'iniciar_sesion.html')

def recervas(request):
    return render(request, 'recervasDu.html')

def registrarMenu(request):
    return render(request, 'registrar.html')

def registrarCliente(request):
    return render(request, 'registroClien.html')

def registrarDuenio(request):
    return render(request, 'registroDu.html')