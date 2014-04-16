# coding: utf-8

from .models import Member


def membros_list(request):
    """
        A listagem de membros será exibida
        em todas as telas, dessa forma foi criado
        o context para que seja possivel acessar
        sempre os membros.
    """
    listagem = Member.objects.all().order_by('?')[:10]
    return {
        'membros': listagem
    }
