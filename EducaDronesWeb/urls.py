from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('integrantes/', views.integrantes, name='integrantes'),
]
