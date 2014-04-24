# coding: utf-8

from django.contrib import admin

from .models import Empresas


class EmpresaAdmin(admin.ModelAdmin):

    search_fields = ('nome',)


admin.site.register(Empresas, EmpresaAdmin)
