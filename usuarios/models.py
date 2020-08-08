from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=32, unique=False, null=False)
    apellido = models.CharField(max_length=32, unique=False, null=False)
    institucion = models.TextField(unique=False, null=False)
    descripcion_personal = models.TextField(max_length=500, blank=True)
    pais = models.CharField(max_length=30, blank=True)
    ciudad = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, blank=False)
    telefono = PhoneNumberField(blank=True)
