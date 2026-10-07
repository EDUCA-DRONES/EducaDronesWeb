from django.core.mail import send_mail
from django.shortcuts import render
from .forms import Contato
# from EducaDronesWeb.views import home


def process_form(request):
    form = Contato(request.POST)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        telefone = form.cleaned_data['telefone']
        instituicao = form.cleaned_data['instituicao']
        cidade = form.cleaned_data['cidade']

        assunto = 'Recebemos sua solicitação - Educa Drones'
        mensagem = f"Olá {nome},\n\nRecebemos sua solicitação para participar do Educa Drones. Em breve nossa equipe entrará em contato com você.\n\nAtenciosamente,\nEquipe Educa Drones"

        send_mail(
            subject=assunto,
            message=mensagem,
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )

        return Contato()
    else:
        form = Contato()
        return form
