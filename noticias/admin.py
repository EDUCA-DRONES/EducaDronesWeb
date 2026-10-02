from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'categoria',
        'data_publicacao',
        'destaque_home',
        'conquista_destaque',
    )

    list_filter = (
        'categoria',
        'destaque_home',
        'conquista_destaque',
    )

    search_fields = (
        'titulo',
        'resumo',
        'conteudo',
    )

    prepopulated_fields = {
        'slug': ('titulo',)
    }

    list_editable = (
        'destaque_home',
        'conquista_destaque',
    )