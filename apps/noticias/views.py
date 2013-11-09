# coding: utf-8
from django.shortcuts import render
from django.http import Http404

from .models import Noticia

def listagem(request):
	return render(request, 'index.html', {'noticias': Noticia.objects.order_by('-data')[:5]})

def detalhe(request, id):
	try:
		noticia = Noticia.objects.get(pk=id)
	except Noticia.DoesNotExist:
		raise Http404
	return render(request, 'noticias/detalhe.html', {'noticia': noticia})
