# coding: utf-8

from django.contrib import admin

from .models import *

admin.site.register(Organizador)
admin.site.register(Evento)
admin.site.register(Programacao)