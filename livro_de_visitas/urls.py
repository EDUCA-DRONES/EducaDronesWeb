from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_redirect, name="form_redirect"),
    path("formulario/", views.formulario, name="formulario"),
    path("api/mapa-impacto/", views.mapa_impacto, name="mapa_impacto"),
]