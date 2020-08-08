from django.db import models
from multiselectfield import MultiSelectField
from usuarios.models import PerfilUsuario

# Create your models here.

class TiposTopicos(models.Model):
    nombre = models.CharField(max_length=256)


class PerfilPonentes(models.Model):
    #usuario =
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, unique=True, null=False, blank=False, default='A definir')
    bio_corto = models.TextField(unique=False, null=False)
    linkedin = models.TextField(unique=True, null=True)
    exp_personales_bool = models.BooleanField()


class TopicosOfrecidos(models.Model):
    fecha = models.DateField(auto_now_add=True)
    ponente = models.ForeignKey(PerfilPonentes, on_delete=models.DO_NOTHING, blank=False, null=False, default="A definir")
    nombre = models.CharField(max_length=256, unique=True, blank=False, null=False)
    categoria = models.ForeignKey(TiposTopicos, on_delete=models.DO_NOTHING, blank=False, null=False)


class PerfilSolicitante(models.Model):
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)

    #topicos =


class TopicosSolicitados(models.Model):
    fecha = models.DateField()
    solicitante = models.ForeignKey(PerfilSolicitante, on_delete=models.DO_NOTHING, blank=False, null=False)
    categoria = models.ForeignKey(TiposTopicos, on_delete=models.DO_NOTHING, blank=False, null=False)

