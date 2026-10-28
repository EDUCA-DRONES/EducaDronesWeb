from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Visitante
from .forms import VisitanteForm

import datetime
from time import sleep


def form_redirect(request):
    return redirect('formulario')


def formulario(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            validacao = Visitante.objects.filter(data_visita=datetime.date.today()).filter(
                telefone=form.cleaned_data['telefone']).exists()
            if validacao:
                return HttpResponse("Você já enviou o formulário hoje")

            form.save()
            return HttpResponse("Formulário enviado com sucesso!")

    else:
        form = VisitanteForm()
    return render(request, 'livro_de_visitas/formulario.html', {'form': form})
