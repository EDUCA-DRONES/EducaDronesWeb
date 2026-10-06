from django.shortcuts import redirect, render
from noticias.models import Noticia
from emails.views import process_form
from emails.forms import Contato


def home(request):

    if request.method == "POST":
        form = process_form(request)
    else:
        form = Contato()

    noticias = Noticia.objects.filter(
        destaque_home=True
    )[:3]

    conquistas = Noticia.objects.filter(
        conquista_destaque=True
    )[:4]

    return render(
        request,
        'home.html',
        {
            'noticias': noticias,
            'conquistas': conquistas,
            'form': form
        }
    )


def sobre(request):
    return render(request, 'sobre/sobrenos.html')


def integrantes(request):
    return render(request, 'integrantes/nossotime.html')
