# coding: utf-8

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.serializers import serialize

from .models import Membro
from .forms import MembroForm


def cadastrar(request, template='membros/cadastrar.html'):
    form = MembroForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        obj = form.save()
        url = reverse('membro_detalhe', kwargs={'id': obj.pk})
        return redirect(url, {'mensagem': 'Salvo com sucesso !'})

    return render(request, template, {'formset': form})


def detalhe(request, id, template='membros/detalhe.html'):
    membro = get_object_or_404(Membro, pk=id)
    return render(request, template, {'membro': membro})


def consultar_por_nome(request, template='membros/listagem.html'):
    name = request.GET.get('name', '')
    membros = Membro.objects.filter(nome__icontains=name)[:5]
    return render(request, template, {'membros': membros})


"""
class Detalhe(DetailView):
    model = Membro
    context_object_name = 'membro'
    template_name = 'membro/detalhe.html
"""