# coding: utf-8

from django.http import HttpResponse


def cadastrar(request):
	return HttpResponse(u'Página de cadastro dos Participantes')

def listagem(request):
    return HttpResponse(u'Página inicial dos Participantes')