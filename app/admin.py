from django.contrib import admin
from .models import PerfilSolicitante, PerfilPonentes, TopicosSolicitados, TopicosOfrecidos, TiposTopicos


# Register your models here.
admin.site.register(TiposTopicos)
admin.site.register(TopicosOfrecidos)
admin.site.register(PerfilSolicitante)
admin.site.register(PerfilPonentes)
admin.site.register(TopicosSolicitados)