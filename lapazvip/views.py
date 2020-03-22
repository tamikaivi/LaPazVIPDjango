from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render


def home(request):
    documento_exter=open("lapazvip/plantillas/home.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def crearServicio(request):
    documento_exter=open("lapazvip/plantillas/crearServicioDu.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def detalle(request):
    documento_exter=open("lapazvip/plantillas/detalle.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def homeSinInicio(request):
    documento_exter=open("lapazvip/plantillas/home_sin_inicio.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def inicioSesion(request):
    documento_exter=open("lapazvip/plantillas/iniciar_sesion.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def recervas(request):
    documento_exter=open("lapazvip/plantillas/recervasDu.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def registrarMenu(request):
    documento_exter=open("lapazvip/plantillas/registrar.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def registrarCliente(request):
    documento_exter=open("lapazvip/plantillas/registroClien.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)

def registrarDuenio(request):
    documento_exter=open("lapazvip/plantillas/registroDu.html")
    plo=Template(documento_exter.read())
    documento_exter.close()
    cont=Context()
    doc=plo.render(cont)
    return HttpResponse(doc)