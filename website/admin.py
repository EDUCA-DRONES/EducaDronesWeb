from django.contrib import admin
from .models import MembroEquipe


@admin.register(MembroEquipe)
class MembroEquipeAdmin(admin.ModelAdmin):

    list_display = ('nome', 'funcao', 'categoria', 'ordem', 'ativo')

    list_filter = ('categoria', 'ativo')

    search_fields = ('nome', 'funcao')

    list_editable = ('ordem', 'ativo')

    ordering = ('categoria', 'ordem', 'nome')