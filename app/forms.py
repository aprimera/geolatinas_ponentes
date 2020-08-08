from django import forms
from app.models import TopicosSolicitados


class SolicitudForma(forms.ModelForm):
    class Meta:
        model = TopicosSolicitados
        exclude =['fecha']
