# coding: utf-8

from django.contrib import admin

from ..common.decorators import attr_decorator
from ..common.admin import firstletterfilter

from .models import Evento, Programacao, Organizador


class InlineProgramacao(admin.TabularInline):
    model = Programacao
    extra = 1


class EventoAdmin(admin.ModelAdmin):
    inlines = [
        InlineProgramacao
    ]

    list_display = ('nome', 'descricao', 'data', 'show_url')
    date_hierarchy = 'data'
    list_filter = ('data', firstletterfilter('nome'))

    @attr_decorator(short_description='url', allow_tags=True, admin_order_field='url')
    def show_url(self, obj):
        return '<a target="_blank" href="{0}">{0}</a>'.format(obj.url)


class OrganizadorAdmin(admin.ModelAdmin):
    list_display = ('show_imagem', 'nome', 'url')
    list_filter = (firstletterfilter('nome'),)

    @attr_decorator(short_description='imagem', allow_tags=True, admin_order_field='nome')
    def show_imagem(self, obj):
        return '<img src="{0}" width="100px" height="100px" />'.format(
            obj.imagem.url)


admin.site.register(Evento, EventoAdmin)
admin.site.register(Organizador, OrganizadorAdmin)
