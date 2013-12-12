# coding: utf-8

from django.contrib import admin

from .models import Projeto

from ..common.decorators import attr_decorator


class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'show_url', 'criado', 'atualizado')

    @attr_decorator(short_description='url', allow_tags=True)
    def show_url(self, obj):
        if obj.url:
            return '<a href="{0}" target="_blank">{0}</a>'.format(obj.url)
        return


admin.site.register(Projeto, ProjetoAdmin)
