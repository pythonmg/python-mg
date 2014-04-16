# coding: utf-8

from django.shortcuts import render

from .noticias.models import Noticia


def home(request, template='v2/index.html'):
    noticias = Noticia.objects.order_by('-data')[:5]
    context = {
        'principal': noticias[0] if noticias else None,
        'noticias': noticias[1:]
    }
    return render(request, template, context)
