# coding: utf-8

from .models import Projeto


def projetos_atualizados(request):
    """
        Irá aparecer na base.html os últimos projetos atualizados,
        sempre no footer. Por isso foi criado um context_processors.
    """
    projetos = Projeto.objects.all()[:5]

    return {
        'projetos': projetos
    }
