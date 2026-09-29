from django.shortcuts import redirect, render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre/sobrenos.html')

def integrantes(request):
    return render(request, 'integrantes/nossotime.html')