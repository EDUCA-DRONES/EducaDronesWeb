from django.urls import path

from . import views


urlpatterns = [
    path("", views.form_redirect, name="form_redirect"),
    path("formulario/", views.formulario, name="formulario"),
    # path("integrantes/", views.integrantes, name="integrantes"),
    # path("noticias/", views.noticias, name="noticias"),
]
