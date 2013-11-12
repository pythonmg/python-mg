# coding: utf-8

from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Participante
from .forms import ParticipanteForm


def cadastrar(request, template='participantes/cadastrar.html'):
    form = ParticipanteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save()
        url = reverse('participante_detalhe', kwargs={'id': obj.pk})
        return redirect(url, {'mensagem': 'Salvo com sucesso !'})

    return render(request, template, {'formset': form})


def detalhe(request, id, template='participantes/detalhe.html'):
    participante = get_object_or_404(Participante, pk=id)
    return render(request, template, {'participante': participante})


def listagem(request, template='participantes/listagem.html'):
    lista = Participante.objects.filter(aprovado=True).order_by('nome')
    return render(request, template, {'lista': lista})
