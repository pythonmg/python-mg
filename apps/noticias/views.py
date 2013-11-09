# coding: utf-8
from django.shortcuts import render

from .models import Noticia

def home(request):
	listagem = Noticia.objects.order_by('-data')[:5]
	context = { 'listagem': listagem }
	return render(request, 'index.html', context)