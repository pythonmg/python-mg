# coding: utf-8

from django.shortcuts import render, get_object_or_404

from .models import Noticia


def detalhe(request, id, template='noticias/detalhe.html'):

    noticia = get_object_or_404(Noticia, pk=id)
    noticia.visualizacoes += 1
    noticia.save()

    context = {
        'noticia': noticia
    }

    return render(request, template, context)
