# coding: utf-8
from django.shortcuts import render

from apps.noticias.models import Noticia
from apps.participantes.models import Participante

def home(request):
	context = {'noticias': Noticia.objects.order_by('-data')[:5],
		'participantes': Participante.objects.all()}
	return render(request, 'index.html', context)