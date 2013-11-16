# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Noticia


def listagem(request, template = 'noticias/listagem.html'):
	noticias_list = Noticia.objects.order_by('-data')[:20]
	paginator = Paginator(noticias_list, 5) # Mostra 5 noticias por pagina

	# Esteja certo de que o page request e um inteiro. Se nao, mostre a primeira
	# pagina
	num_page = request.GET.get('page')
	try:
		page_noticias = paginator.page(num_page)
	except PageNotAnInteger:
		page_noticias = paginator.page(1)
	except EmptyPage:
		page_noticias = paginator.page(paginator.num_pages)

	return render(request, template, {'noticias': page_noticias })

def detalhe(request, id):
    noticia = get_object_or_404(Noticia, pk=id)
    return render(request, 'noticias/detalhe.html', {'noticia': noticia})
