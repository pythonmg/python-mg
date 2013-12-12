from django.shortcuts import render, get_object_or_404

from .models import Projeto


def detalhe(request, id, template='projetos/detalhe.html'):
    projeto = get_object_or_404(Projeto, pk=id)

    context = {
        'projeto': projeto
    }

    return render(request, template, context)
