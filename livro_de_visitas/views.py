import datetime
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import VisitanteForm
from .models import CidadeCoordenadas, Visitante


def form_redirect(request):
    return redirect("formulario")


def formulario(request):
    if request.method == "POST":
        form = VisitanteForm(request.POST)

        if form.is_valid():

            form.save(commit=False)
            form.instance.cidade = form.cleaned_data["cidade"].title()
            form.instance.nome = form.cleaned_data["nome"].title()

            validacao = Visitante.objects.filter(
                data_visita=datetime.date.today(),
                telefone=form.cleaned_data["telefone"],
                nome=form.cleaned_data["nome"].title(),
                cidade=form.cleaned_data["cidade"].title(),
                estado=form.cleaned_data["estado"],
                data_nascimento=form.cleaned_data["data_nascimento"],
                genero=form.cleaned_data["genero"]
            ).exists()

            if validacao:
                messages.error(request, "Você já enviou o formulário hoje")
                return redirect("formulario")

            form.save(commit=True)
            
            messages.success(request, "Formulário enviado com sucesso!")
            return redirect("formulario")

    else:
        form = VisitanteForm()

    return render(
        request,
        "livro_de_visitas/formulario.html",
        {"form": form},
    )


def mapa_impacto(request):
    coordenadas = {
        (item.cidade.casefold(), item.estado.upper()): item
        for item in CidadeCoordenadas.objects.all()
    }

    registros = (
        Visitante.objects.values("cidade", "estado")
        .annotate(total=Count("id"))
        .order_by("cidade", "estado")
    )

    locais = []

    for registro in registros:
        chave = (
            registro["cidade"].strip().casefold(),
            registro["estado"].strip().upper(),
        )

        coordenada = coordenadas.get(chave)

        if coordenada:
            locais.append({
                "cidade": coordenada.cidade,
                "estado": coordenada.estado,
                "latitude": coordenada.latitude,
                "longitude": coordenada.longitude,
                "total": registro["total"],
            })

    return JsonResponse({
        "total_pessoas": Visitante.objects.count(),
        "total_cidades": len(locais),
        "locais": locais,
    })
