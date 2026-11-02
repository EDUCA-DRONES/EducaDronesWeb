from django.test import TestCase
from django.urls import reverse

from .forms import VisitanteForm
from .models import CidadeCoordenadas, Visitante


class VisitanteModelTests(TestCase):
    def test_string_representation_contains_name_city_and_state(self):
        visitante = Visitante(
            nome="Ana Silva",
            cidade="Guanambi",
            estado="BA",
            genero=Visitante.Genero.FEMININO,
            telefone=None,
            data_nascimento="2000-01-01",
        )

        self.assertEqual(str(visitante), "Ana Silva - Guanambi/BA")


class VisitanteFormTests(TestCase):
    def test_accepts_valid_visitor_data(self):
        form = VisitanteForm(data={
            "nome": "Ana Silva",
            "estado": "BA",
            "cidade": "Guanambi",
            "genero": Visitante.Genero.FEMININO,
            "telefone": "+5577981345831",
            "data_nascimento": "2000-01-01",
        })
        form.fields["cidade"].choices = [
            ("", "Selecione uma cidade"),
            ("Guanambi", "Guanambi"),
        ]

        self.assertTrue(form.is_valid(), form.errors)

    def test_rejects_name_containing_numbers(self):
        form = VisitanteForm(data={
            "nome": "Ana123",
            "estado": "BA",
            "cidade": "Guanambi",
            "genero": Visitante.Genero.FEMININO,
            "telefone": "+5577981345831",
            "data_nascimento": "2000-01-01",
        })
        form.fields["cidade"].choices = [("Guanambi", "Guanambi")]

        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)


class VisitanteViewsTests(TestCase):
    def test_formulario_page_renders_form(self):
        response = self.client.get(reverse("formulario"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "livro_de_visitas/formulario.html")
        self.assertIsInstance(response.context["form"], VisitanteForm)

    def test_impact_map_counts_visitors_and_matches_coordinates(self):
        CidadeCoordenadas.objects.create(
            cidade="Guanambi",
            estado="BA",
            latitude=-14.223,
            longitude=-42.779,
        )
        Visitante.objects.create(
            nome="Ana Silva",
            estado="BA",
            cidade="Guanambi",
            genero=Visitante.Genero.FEMININO,
            telefone=None,
            data_nascimento="2000-01-01",
        )
        Visitante.objects.create(
            nome="Bruno Souza",
            estado="BA",
            cidade="Guanambi",
            genero=Visitante.Genero.MASCULINO,
            telefone=None,
            data_nascimento="1999-02-01",
        )
        Visitante.objects.create(
            nome="Carla Costa",
            estado="SP",
            cidade="São Paulo",
            genero=Visitante.Genero.NAO_BINARIO,
            telefone=None,
            data_nascimento="2001-03-01",
        )

        response = self.client.get(reverse("mapa_impacto"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "total_pessoas": 3,
            "total_cidades": 1,
            "locais": [{
                "cidade": "Guanambi",
                "estado": "BA",
                "latitude": -14.223,
                "longitude": -42.779,
                "total": 2,
            }],
        })
