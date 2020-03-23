from django.db import models

# Create your models here.
class Duenio(models.Model):
    nombre=models.CharField(max_length=200)
    correo=models.EmailField()
    password=models.CharField(max_length=200)
    telefono=models.IntegerField()
    direccion=models.TextField()

    def __str__(self):
        return self.nombre