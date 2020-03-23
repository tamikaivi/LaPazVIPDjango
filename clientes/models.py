from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=200)
    correo=models.EmailField()
    password=models.CharField(max_length=100)
    telefono=models.IntegerField()
    ciudad=models.CharField(max_length=500)

    def __str__(self):
        return self.nombre