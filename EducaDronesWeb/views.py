from django.shortcuts import redirect, render
from noticias.models import Noticia


def home(request):

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
        }
    )


def sobre(request):
    return render(request, 'sobre/sobrenos.html')


def integrantes(request):
    return render(request, 'integrantes/nossotime.html')

def noticias(request):
    noticias = Noticia.objects.filter(destaque_home=True)

    return render(
        request,
        'Noticias/noticias.html',
        {
            'noticias': noticias,
        }
    )