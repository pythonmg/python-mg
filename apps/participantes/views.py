# coding: utf-8

from django.http import HttpResponse


def listagem(request):
    return HttpResponse(u'Página inicial dos Participantes')