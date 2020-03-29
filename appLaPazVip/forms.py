from django import forms
from . import models

class CreateUser(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.Cliente
        fields= ['nombre','correo','password','telefono','ciudad']

class CreateDuenio(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = models.Duenio
        fields= ['nombre','correo','password','telefono','direccion']

class CreateServicio(forms.ModelForm):
    class Meta:
        model = models.Servicio
        fields= ['nombre','imagen','descripcion','contacto','zona','precio','tipo','duenio']

class DateForm(forms.Form):
    date = forms.DateTimeField()