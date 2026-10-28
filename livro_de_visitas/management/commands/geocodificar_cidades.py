import json
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from django.core.management.base import BaseCommand
from django.db.models import Count

from livro_de_visitas.models import CidadeCoordenadas, Visitante


class Command(BaseCommand):
    help = "Busca as coordenadas das cidades registradas no livro de visitas."

    def handle(self, *args, **options):
        cidades = (
            Visitante.objects.values("cidade", "estado")
            .annotate(total=Count("id"))
            .order_by("cidade", "estado")
        )

        cadastradas = 0
        ignoradas = 0

        for item in cidades:
            cidade = item["cidade"].strip()
            estado = item["estado"].strip().upper()

            if not cidade or not estado:
                ignoradas += 1
                continue

            existe = CidadeCoordenadas.objects.filter(
                cidade__iexact=cidade,
                estado__iexact=estado,
            ).exists()

            if existe:
                continue

            parametros = urlencode({
                "city": cidade,
                "state": estado,
                "country": "Brasil",
                "countrycodes": "br",
                "format": "jsonv2",
                "limit": 1,
            })

            url = f"https://nominatim.openstreetmap.org/search?{parametros}"
            requisicao = Request(
                url,
                headers={"User-Agent": "EducaDronesWeb/1.0"},
            )

            try:
                with urlopen(requisicao, timeout=15) as resposta:
                    resultados = json.loads(resposta.read().decode("utf-8"))

                if not resultados:
                    self.stdout.write(
                        self.style.WARNING(
                            f"Coordenadas não encontradas: {cidade}/{estado}"
                        )
                    )
                    ignoradas += 1
                    continue

                resultado = resultados[0]

                CidadeCoordenadas.objects.create(
                    cidade=cidade,
                    estado=estado,
                    latitude=float(resultado["lat"]),
                    longitude=float(resultado["lon"]),
                )

                cadastradas += 1
                self.stdout.write(f"Coordenadas cadastradas: {cidade}/{estado}")

            except (HTTPError, URLError, TimeoutError, ValueError, KeyError) as erro:
                self.stdout.write(
                    self.style.ERROR(f"Erro em {cidade}/{estado}: {erro}")
                )
                ignoradas += 1

            time.sleep(1.1)

        self.stdout.write(
            self.style.SUCCESS(
                f"Concluído. Cidades cadastradas: {cadastradas}. "
                f"Ignoradas ou com erro: {ignoradas}."
            )
        )