from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Visitante(models.Model):
    class Genero(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        NAO_BINARIO = 'NB', 'Não Binário'
        PREFIRO_NAO_RESPONDER = 'NR', 'Prefiro Não Responder'

    class Estados(models.TextChoices):
        AC = 'AC', 'Acre'
        AL = 'AL', 'Alagoas'
        AP = 'AP', 'Amapá'
        AM = 'AM', 'Amazonas'
        BA = 'BA', 'Bahia'
        CE = 'CE', 'Ceará'
        DF = 'DF', 'Distrito Federal'
        ES = 'ES', 'Espírito Santo'
        GO = 'GO', 'Goiás'
        MA = 'MA', 'Maranhão'
        MT = 'MT', 'Mato Grosso'
        MS = 'MS', 'Mato Grosso do Sul'
        MG = 'MG', 'Minas Gerais'
        PA = 'PA', 'Pará'
        PB = 'PB', 'Paraíba'
        PR = 'PR', 'Paraná'
        PE = 'PE', 'Pernambuco'
        PI = 'PI', 'Piauí'
        RJ = 'RJ', 'Rio de Janeiro'
        RN = 'RN', 'Rio Grande do Norte'
        RS = 'RS', 'Rio Grande do Sul'
        RO = 'RO', 'Rondônia'
        RR = 'RR', 'Roraima'
        SC = 'SC', 'Santa Catarina'
        SP = 'SP', 'São Paulo'
        SE = 'SE', 'Sergipe'
        TO = 'TO', 'Tocantins'

    nome = models.CharField(max_length=200)
    estado = models.CharField(max_length=2, choices=Estados.choices)
    cidade = models.CharField(max_length=50)
    genero = models.CharField(
        max_length=2, choices=Genero.choices, default=None)
    telefone = PhoneNumberField(region="BR", null=True)
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
