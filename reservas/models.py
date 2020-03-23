from django.db import models
from clientes.models import Cliente
from servicios.models import Servicio
# Create your models here.
class Reserva(models.Model):
    fecha=models.DateField()
    cliente=models.ForeignKey(Cliente,default=None,on_delete=models.CASCADE)
    servicio=models.ForeignKey(Servicio,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha