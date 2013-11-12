# coding: utf-8

from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import redirect, render

from .models import Participante
from .forms import ParticipanteForm

def cadastrar(request, template='participantes/cadastrar.html'):
	if request.method == 'POST':
		form = ParticipanteForm(request.POST, request.FILES)
		print form.is_valid()
		if form.is_valid():
			obj = form.save()
			return redirect('/participantes/%d/' % obj.pk, {'menagem': 'Salvo com sucesso !'})
	else:
		form = ParticipanteForm()
	return render(request, template, {'formset': form})


def detalhe(request, id, template='participantes/detalhe.html'):
	try:
		participante = Participante.objects.get(pk=id)
	except Participante.DoesNotExist:
		raise Http404
	return render(request, template, {'participante': participante})