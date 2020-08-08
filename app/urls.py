from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.dca_main, name="dca_main"),
    path('ingreso/', views.dca_main, name="dca_main"),
    path('solicitar_ponente/', views.dca_create, name="dca_create"),
    path('ofrecer_ponencia/', views.dca_create, name="dca_create"),
    path('lista_solicitudes/<int:id>', views.dca_open, name="dca_open"),
    path('lista_ponencias/<int:id>', views.dca_edit_case, name="dca_edit"),
    ]
