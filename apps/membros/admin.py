# coding: utf-8

from django.contrib import admin
"""
from ..common.decorators import attr_decorator
from ..common.admin import firstletterfilter
"""
from .models import Member

"""
class MembroAdmin(admin.ModelAdmin):
    list_display = ('show_imagem', 'nome', 'email',
                    'data_nascimento', 'genero', 'show_url')
    list_filter = ('genero', 'aprovado', firstletterfilter('nome'))
    search_fields = ('nome', 'email')

    date_hierarchy = 'cadastrado'

    @attr_decorator(short_description='imagem', allow_tags=True)
    def show_imagem(self, obj):
        if obj.foto:
            return '<img src="{}" width="100px" height="100px"/>'.format(
                obj.foto.url)
        return None

    @attr_decorator(short_description='url', allow_tags=True)
    def show_url(self, obj):
        if obj.url:
            return '<a href="{0}" target="_blank">{0}</a>'.format(obj.url)
        return

admin.site.register(Membro, MembroAdmin)
"""

admin.site.register(Member)
