# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.shortcuts import render_to_response
from django.template import RequestContext

# Third-party app imports

# Imports from your apps
from .forms import ContribuicaoForm
from .models import Contribuicoes
from apps.noticias.models import Noticia


def contribuicao(request):
    """
    View para salvar os dados do post do formulario
    de contribuicao
    """
    if request.method == 'POST':
        form = ContribuicaoForm(request.POST, request.FILES,)
        if form.is_valid():
            contribuicao = form.save(commit=False)
        else:
            form = ContribuicaoForm()
        contribuicao.save()
    else:
        form = ContribuicaoForm()
    noticias = Noticia.objects.order_by('-data')[:5]
    return render_to_response(
        'index.html',
        {
            'form': form,
            'principal': noticias[0] if noticias else None,
            'noticias': noticias[1:],
        },
        context_instance=RequestContext(request)
    )
