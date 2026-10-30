from django.shortcuts import render, get_object_or_404

from emails.forms import Contato
from emails.views import process_form
from noticias.models import Noticia


def home(request):
    if request.method == "POST":
        form = process_form(request)
    else:
        form = Contato()

    noticias = Noticia.objects.filter(destaque_home=True)[:3]
    conquistas = Noticia.objects.filter(conquista_destaque=True)[:4]

    return render(
        request,
        "home.html",
        {
            "noticias": noticias,
            "conquistas": conquistas,
            "form": form,
        },
    )


def sobre(request):
    return render(request, "Sobre/sobrenos.html")


def integrantes(request):
    return render(request, "Integrantes/nossotime.html")


def noticias(request):
    noticias = Noticia.objects.filter(destaque_home=True)

    return render(
        request,
        "Noticias/noticias.html",
        {"noticias": noticias},
    )


def noticia_detalhe(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)

    return render(
        request,
        "Noticias/noticia_detalhe.html",
        {"noticia": noticia},
    )