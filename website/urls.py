from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("integrantes/", views.integrantes, name="integrantes"),
    path("noticias/", views.noticias, name="noticias"),
    path("noticias/<slug:slug>/", views.noticia_detalhe, name="noticia_detalhe", ),
    path("obadrones/", views.obadrones, name="obadrones"),
    path("colibri/", views.colibri, name="colibri")
]