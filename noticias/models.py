from django.db import models
from django.utils.text import slugify


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    categoria = models.CharField(max_length=100)
    data_publicacao = models.DateField()
    imagem = models.ImageField(upload_to='noticias/')
    resumo = models.TextField(max_length=500)
    conteudo = models.TextField()

    destaque_home = models.BooleanField(
        default=False,
        verbose_name='Exibir em Notícias e Eventos'
    )

    conquista_destaque = models.BooleanField(
        default=False,
        verbose_name='Exibir em Conquistas que falam por Si'
    )

    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo