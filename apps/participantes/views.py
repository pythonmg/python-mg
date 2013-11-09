# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render

def cadastrar(request):
	return HttpResponse(u'Página de cadastro dos Participantes')

def listagem(request):
    #return HttpResponse(u'Página inicial dos Participantes')
    return render(request, 'index.html')
