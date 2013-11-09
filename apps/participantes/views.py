# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render

from .models import Participante

def cadastrar(request):
	return HttpResponse(u'Página de cadastro dos Participantes')

def listagem():
	return render(request, 'index.html', {'participantes': Participante.objects.all()})