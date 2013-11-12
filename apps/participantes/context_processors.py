# coding: utf-8

from .models import Participante


def participantes_list(request):
    """
        A listagem de participante será exibida
        em todas as telas, dessa forma foi criado
        o context para que seja possivel acessar
        sempre os participantes.
    """
    return {
        'participantes': Participante.objects.filter(aprovado=True),
    }