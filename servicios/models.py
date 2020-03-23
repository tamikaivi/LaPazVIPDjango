from django.db import models
from duenios.models import Duenio
# Create your models here.
class Servicio(models.Model):
    nombre=models.CharField(max_length=500)
    imagen=models.ImageField()
    descripcion=models.TextField()
    contacto=models.IntegerField()
    zona=models.TextField()
    precio=models.IntegerField()
    tipo=models.CharField(max_length=50)
    duenio=models.ForeignKey(Duenio, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    #def snippet(self):
     #   return self.descripcion[:50]+'...'