#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Member
from .forms import MembroForm


@login_required
def redirect_form(request, template='membros/cadastrar.html'):
    if request.user.member_profile:
        return redirect('done')

    form = MembroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        member = form.save(commit=False)
        member.user = request.user
        member.save()
        return redirect('done')
    
    return render(request, template, {'formset': form})

@login_required
def done(request):
    if request.user.member_profile:
        """Login complete view, display user data"""
        return render(request, 'done.html',{'member': member})
    else:
        return redirect('redirect_form')

def detalhe(request, id, template='membros/detalhe.html'):
    membro = get_object_or_404(Member, pk=id)
    return render(request, template, {'membro': membro})


def consultar_por_nome(request, template='membros/listagem.html'):
    name = request.GET.get('name', '')
    membros = Member.objects.filter(nome__icontains=name, aprovado=True)[:5]
    return render(request, template, {'membros': membros})
