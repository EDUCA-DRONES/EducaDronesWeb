from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Visitante(models.Model):
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        NAO_BINARIO = 'NB', 'Não Binário'
        PREFIRO_NAO_RESPONDER = 'NR', 'Prefiro Não Responder'

    nome = models.CharField(max_length=200)
    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    genero = models.CharField(max_length=2, choices=Genero.choices, default=None)
    telefone = PhoneNumberField(region="BR", blank=True, null=True)
    data_nascimento = models.DateField(null=False)
    data_visita = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.cidade}/{self.estado}"


class CidadeCoordenadas(models.Model):
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cidade", "estado"],
                name="cidade_estado_coordenadas_unicas",
            )
        ]

    def __str__(self):
        return f"{self.cidade}/{self.estado}"
