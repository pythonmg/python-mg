# coding: utf-8

from django.shortcuts import render

from .noticias.models import Noticia


def home(request, template='index.html'):
    noticias = Noticia.objects.order_by('-data')[:5]
    return render(request, template, {'noticias': noticias})