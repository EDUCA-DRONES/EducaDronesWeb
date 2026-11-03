from django.db import models


class MembroEquipe(models.Model):

    CATEGORIAS = [
        ('pesquisador', 'Pesquisadores'),
        ('aluno', 'Alunos e Egressos'),
    ]

    nome = models.CharField(max_length=150)
    funcao = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    foto = models.ImageField(upload_to='integrantes/', blank=True, null=True)

    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Integrante'
        verbose_name_plural = 'Integrantes da equipe'
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome