from django.test import TestCase
from django.urls import reverse

from noticias.models import Noticia


class WebsiteViewTests(TestCase):
    def test_static_pages_render_successfully(self):
        for route_name in ("home", "sobre", "integrantes", "obadrones", "colibri"):
            with self.subTest(route=route_name):
                response = self.client.get(reverse(route_name))
                self.assertEqual(response.status_code, 200)

    def test_home_shows_only_highlighted_news_and_achievements(self):
        noticia_destaque = self.create_noticia(
            "Notícia em destaque",
            "noticia-destaque",
            destaque_home=True,
        )
        conquista = self.create_noticia(
            "Conquista em destaque",
            "conquista-destaque",
            conquista_destaque=True,
        )
        self.create_noticia("Notícia não destacada", "nao-destacada")

        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["noticias"]), [noticia_destaque])
        self.assertEqual(list(response.context["conquistas"]), [conquista])

    def test_news_page_lists_home_highlights_only(self):
        destaque = self.create_noticia(
            "Notícia em destaque",
            "noticia-destaque",
            destaque_home=True,
        )
        self.create_noticia("Notícia não destacada", "nao-destacada")

        response = self.client.get(reverse("noticias"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["noticias"]), [destaque])

    def test_news_detail_uses_slug_and_unknown_slug_returns_404(self):
        noticia = self.create_noticia(
            "Notícia publicada",
            "noticia-publicada",
        )

        response = self.client.get(
            reverse("noticia_detalhe", kwargs={"slug": noticia.slug})
        )
        missing_response = self.client.get(
            reverse("noticia_detalhe", kwargs={"slug": "nao-existe"})
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["noticia"], noticia)
        self.assertEqual(missing_response.status_code, 404)

    def create_noticia(
        self,
        titulo,
        slug,
        *,
        destaque_home=False,
        conquista_destaque=False,
    ):
        return Noticia.objects.create(
            titulo=titulo,
            slug=slug,
            categoria="Projeto",
            data_publicacao="2026-01-15",
            imagem="noticias/drones.jpg",
            resumo="Resumo da notícia",
            conteudo="Conteúdo completo da notícia",
            destaque_home=destaque_home,
            conquista_destaque=conquista_destaque,
        )
