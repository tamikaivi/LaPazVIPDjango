from django.shortcuts import render
from .models import *
from . import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    if request.method=='GET':
        start_date = request.GET.get('start_date')
        if start_date==None:
            servicios = Servicio.objects.all()
            return render(request, 'home.html', {'servicios': servicios})
        else:
            reservas= Reserva.objects.filter(fecha=start_date)
            servicios_reservados = [x.servicio for x in reservas]
            servicios = Servicio.objects.exclude(nombre__in=servicios_reservados)
            return render(request, 'home.html', {'servicios': servicios})
    else:
        servicios = Servicio.objects.all()
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
    if request.method=='POST':
        form = forms.CreateServicio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = forms.CreateServicio()
        return render(request, 'crearServicioDu.html', {'formset': form})
    return render(request, 'crearServicioDu.html', {'formset': form})



def detalle(request, nombre):
    servicio= Servicio.objects.get(nombre=nombre)
    return render(request, 'detalle.html', {'servicio': servicio})

def homeSinInicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'home_sin_inicio.html', {'servicios': servicios})

def inicioSesion(request):
    return render(request, 'iniciar_sesion.html')

def reservas(request):
    reservas= Reserva.objects.all()
    return render(request, 'reservasDu.html',{'reservas':reservas})

def registrarMenu(request):
    return render(request, 'registrar.html')

def registrarCliente(request):
    if request.method=='POST':
        form = forms.CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeSin')
    else:
        form = forms.CreateUser()
        return render(request, 'registroClien.html', {'formset': form})
    return render(request, 'registroClien.html', {'formset': form})

def registrarDuenio(request):
    if request.method == 'POST':
        form = forms.CreateDuenio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = forms.CreateDuenio()
        return render(request, 'registroDu.html', {'formset': form})
    return render(request, 'registroDu.html',{'formset':form})
