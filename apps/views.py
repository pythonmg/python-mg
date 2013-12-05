# coding: utf-8

from django.shortcuts import render

from .noticias.models import Noticia


def home(request, template='index.html'):
    noticias = Noticia.objects.order_by('-data')[:5]
    principal = None
    if noticias:
        principal = noticias[0]
        noticias = noticias[1:]
    return render(request, template, {'principal':principal,'noticias': noticias})
