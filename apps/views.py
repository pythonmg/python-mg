# coding: utf-8
from django.shortcuts import render, redirect

from .noticias.models import Noticia
from apps.contribuicoes.forms import ContribuicaoForm


def home(request, template='v2/index.html'):
    noticias = Noticia.objects.order_by('-data')[:5]
    context = {
        'principal': noticias[0] if noticias else None,
        'noticias': noticias[1:],
        'form': ContribuicaoForm
    }
    return render(request, template, context)
