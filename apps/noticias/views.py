# coding: utf-8

from django.shortcuts import render, get_object_or_404

from .models import Noticia


def listagem(request):
    return render(
        request,
        'index.html',
        {'noticias': Noticia.objects.order_by('-data')[:5]}
    )


def detalhe(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})
