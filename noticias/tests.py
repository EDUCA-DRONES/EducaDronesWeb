from django.test import TestCase

from .models import Noticia


class NoticiaModelTests(TestCase):
    def test_slug_is_generated_from_title_when_missing(self):
        noticia = Noticia.objects.create(
            titulo="Educa Drones em Guanambi",
            categoria="Projeto",
            data_publicacao="2026-01-15",
            imagem="noticias/drones.jpg",
            resumo="Resumo da notícia",
            conteudo="Conteúdo completo da notícia",
        )

        self.assertEqual(noticia.slug, "educa-drones-em-guanambi")

    def test_custom_slug_is_preserved(self):
        noticia = Noticia.objects.create(
            titulo="Título da notícia",
            slug="slug-personalizado",
            categoria="Projeto",
            data_publicacao="2026-01-15",
            imagem="noticias/drones.jpg",
            resumo="Resumo da notícia",
            conteudo="Conteúdo completo da notícia",
        )

        self.assertEqual(noticia.slug, "slug-personalizado")

    def test_news_are_ordered_by_publication_date_descending(self):
        mais_antiga = Noticia.objects.create(
            titulo="Notícia antiga",
            categoria="Projeto",
            data_publicacao="2026-01-01",
            imagem="noticias/antiga.jpg",
            resumo="Resumo",
            conteudo="Conteúdo",
        )
        mais_recente = Noticia.objects.create(
            titulo="Notícia recente",
            categoria="Projeto",
            data_publicacao="2026-02-01",
            imagem="noticias/recente.jpg",
            resumo="Resumo",
            conteudo="Conteúdo",
        )

        self.assertEqual(
            list(Noticia.objects.all()),
            [mais_recente, mais_antiga],
        )
