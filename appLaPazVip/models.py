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

class Duenio(models.Model):
    nombre=models.CharField(max_length=200)
    correo=models.EmailField()
    password=models.CharField(max_length=200)
    telefono=models.IntegerField()
    direccion=models.TextField()

    def __str__(self):
        return self.nombre
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

    def snippet(self):
        return self.descripcion[:50]+'...'

class Reserva(models.Model):
    fecha=models.DateField()
    cliente=models.ForeignKey(Cliente,default=None,on_delete=models.CASCADE)
    servicio=models.ForeignKey(Servicio,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha)
