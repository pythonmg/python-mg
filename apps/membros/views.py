#!/usr/bin/env python
# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory

from .models import Member, Social
from .forms import MemberForm, SocialFormset


@login_required
def register_final(request, template='membros/v2/register_final.html'):
    if Member.objects.filter(user=request.user).exists():
        return redirect('done')

    form = MemberForm()
    formset = SocialFormset(instance=Member())
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            member = form.save(commit=False)
            member.user = user
            member.save()
            formset = SocialFormset(request.POST, instance=member)
            if formset.is_valid():
                formset.save()
                return redirect('done')
            else:
                return redirec('done')

    return render(request, template, {'form': form, 'formset': formset})


@login_required
def done(request):
    profile = Member.objects.filter(user=request.user)
    if len(profile) > 0:
        """Login complete view, display user data"""
        return render(
            request,
            'membros/done.html',
            {'profile': profile}
        )
    else:
        return redirect('register-final')


def detalhe(request, id, template='membros/detalhe.html'):
    membro = get_object_or_404(Member, pk=id)
    return render(request, template, {'membro': membro})


def consultar_por_nome(request, template='membros/listagem.html'):
    name = request.GET.get('name', '')
    membros = Member.objects.filter(nome__icontains=name, aprovado=True)[:5]
    return render(request, template, {'membros': membros})
