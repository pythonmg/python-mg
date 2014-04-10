# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext as _

# Third-party app imports

# Realative imports of the 'app-name' package
from .models import Contribuicoes


class ContribuicoesAdmin(admin.ModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD da tabela Contribuições
    """

    # campos a serem exibidos na tabela
    list_display = (
        'titulo', 'descricao', 'aprovado', 'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('titulo', 'created', )

    list_filter = ('created', )

admin.site.register(Contribuicoes, ContribuicoesAdmin)
