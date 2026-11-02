from django.test import TestCase
from django.test import RequestFactory
from unittest.mock import patch

from .forms import Contato
from .views import process_form


class ContatoFormTests(TestCase):
    def test_valid_data_and_optional_phone_are_accepted(self):
        form = Contato(data={
            "nome": "Ana Silva",
            "email": "ana@example.com",
            "instituicao": "IF Baiano",
            "cidade": "Guanambi, BA",
        })

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.cleaned_data["telefone"], "")

    def test_invalid_email_is_rejected(self):
        form = Contato(data={
            "nome": "Ana Silva",
            "email": "email-invalido",
            "instituicao": "IF Baiano",
            "cidade": "Guanambi, BA",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_valid_submission_sends_confirmation_to_submitted_email(self):
        request = RequestFactory().post("/", data={
            "nome": "Ana Silva",
            "email": "ana@example.com",
            "telefone": "77981345831",
            "instituicao": "IF Baiano",
            "cidade": "Guanambi, BA",
        })

        with patch("emails.views.send_mail") as send_mail:
            form = process_form(request)

        send_mail.assert_called_once()
        self.assertEqual(send_mail.call_args.kwargs["recipient_list"], [
            "ana@example.com",
        ])
        self.assertIn("Olá Ana Silva", send_mail.call_args.kwargs["message"])
        self.assertFalse(form.is_bound)
