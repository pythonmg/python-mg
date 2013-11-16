# coding: utf-8

from .models import Membro


def membros_list(request):
    """
        A listagem de membros será exibida
        em todas as telas, dessa forma foi criado
        o context para que seja possivel acessar
        sempre os membros.
    """
    listagem = Membro.objects.filter(aprovado=True).order_by('?')[:20]
    return {'membros': listagem}
