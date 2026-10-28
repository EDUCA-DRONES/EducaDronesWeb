from django import forms
from django.core.validators import RegexValidator
from .models import Visitante
from phonenumber_field.formfields import PhoneNumberField as PhoneFormField

validador_letras = RegexValidator(
    regex=r'^[a-zA-ZÀ-ÿ\s]+$',
    message='Este campo deve conter apenas letras e espaços.'
)


class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'estado', 'cidade',
                  'genero', 'telefone', 'data_nascimento']
        widgets = {

            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'telefone': forms.TextInput(attrs={'type': 'tel'}),
            'genero': forms.Select(attrs={'class': 'form-select'}),
            'nome': forms.TextInput(attrs={
                'pattern': '[a-zA-ZÀ-ÿ\s]+',
                'title': 'Apenas letras são permitidas.',
                'oninput': "this.value = this.value.replace(/[^a-zA-ZÀ-ÿ\s]/g, '')"
            }),
            'estado': forms.TextInput(attrs={
                'pattern': '[a-zA-ZÀ-ÿ\s]+',
                'title': 'Apenas letras são permitidas.',
                'oninput': "this.value = this.value.replace(/[^a-zA-ZÀ-ÿ\s]/g, '')"
            }),
            'cidade': forms.TextInput(attrs={
                'pattern': '[a-zA-ZÀ-ÿ\s]+',
                'title': 'Apenas letras são permitidas.',
                'oninput': "this.value = this.value.replace(/[^a-zA-ZÀ-ÿ\s]/g, '')"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['genero'].choices = [
            ('', 'Selecione...')] + Visitante.Genero.choices

        for campo in ['nome', 'estado', 'cidade']:
            if campo in self.fields:
                self.fields[campo].validators.append(validador_letras)
