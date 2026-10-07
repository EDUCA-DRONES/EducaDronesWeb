from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("integrantes/", views.integrantes, name="integrantes"),
    path("noticias/", views.noticias, name="noticias"),
]
