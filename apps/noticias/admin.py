# coding: utf-8

from django.contrib import admin

from .models import Noticia


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'conteudo', 'data', 'visualizacoes', 'usuario')
    list_filter = ('data',)

    date_hierarchy = 'data'
    search_fields = ('titulo', 'conteudo', 'usuario__username')


admin.site.register(Noticia, NoticiaAdmin)
