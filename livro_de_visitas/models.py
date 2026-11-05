from django.db import models


class Visitante(models.Model):
    class FaixaEtaria(models.TextChoices):
        CRIANCA = '1', '0-11 anos'
        ADOLESCENTE = '2', '12-17 anos'
        JOVEM_ADULTO = '3', '18-25'
        ADULTO = '4', '26-59'
        IDOSO = '5', '60+'

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
    faixa_etaria = models.CharField(max_length=1, choices=FaixaEtaria.choices)
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
