from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('crearServicio', crearServicio, name='crearServicio'),
    path('(?P<nombre>[\w-]+)/', detalle, name='detalle'),
    path('homeSinInicio', homeSinInicio, name='homeSin'),
    path('inicioSesion', inicioSesion, name='inicioSesion'),
    path('reservas', reservas, name='reservas'),
    path('registrarMenu', registrarMenu, name='registrarMenu'),
    path('registroCliente', registrarCliente, name='registrarCliente'),
    path('registroDuenio', registrarDuenio, name='registrarDuenio'),
    path('bebidas', bebidas, name='bebidas'),
    path('musica', musica, name='musica'),
    path('locales', locales, name='locales'),

]
urlpatterns+=staticfiles_urlpatterns()