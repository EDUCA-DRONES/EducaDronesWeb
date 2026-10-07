from django import forms


class Contato(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={'id': 'nome', 'placeholder': 'Prof. João Silva', 'required': True})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'id': 'email', 'placeholder': 'exemplo@email.com', 'required': True})
    )
    telefone = forms.CharField(
        max_length=20,
        required=False,  # Opcional
        widget=forms.TextInput(
            attrs={'id': 'telefone', 'type': 'tel', 'placeholder': '(77) 9 9999-9999'})
    )
    instituicao = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={'id': 'instituicao', 'placeholder': 'IF Baiano - Campus...'})
    )
    cidade = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'id': 'cidade', 'placeholder': 'Guanambi, BA'})
    )
