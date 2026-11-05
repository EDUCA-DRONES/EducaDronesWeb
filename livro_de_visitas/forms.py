from django import forms
from django.core.validators import RegexValidator, MinLengthValidator
from .models import Visitante

validador_letras = RegexValidator(
    regex=r'^[a-zA-ZÀ-ÿ ]+$',
    message='Este campo deve conter apenas letras e espaços.'
)


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'estado', 'cidade',
                  'faixa_etaria']
        widgets = {
            'nome': forms.TextInput(attrs={
                'pattern': '[a-zA-ZÀ-ÿ ]+',
                'title': 'Apenas letras são permitidas.',
                'oninput': "this.value = this.value.replace(/[^a-zA-ZÀ-ÿ ]/g, '')",
                'placeholder': 'Digite seu nome...',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'

            }),
            'cidade': forms.Select(attrs={
                'class': 'form-select',
                'disabled': True,
            }),
            'faixa_etaria': forms.Select(attrs={'class': 'form-select', "required": True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['faixa_etaria'].choices = [
            ('', 'Selecione...')] + list(Visitante.FaixaEtaria.choices)

        self.fields['estado'].choices = [
            ('', 'Selecione um Estado...')] + list(Visitante.Estados.choices)

        self.fields['cidade'].choices = [
            ('', 'Selecione um Estado Primeiro...')] + list(Visitante.objects.none())

        for campo in ['nome', 'estado']:
            if campo in self.fields:
                self.fields[campo].validators.append(validador_letras)

        if 'estado' in self.fields:
            self.fields['estado'].validators.append(
                MinLengthValidator(
                    2, message='O estado deve ter exatamente 2 letras.')
            )
