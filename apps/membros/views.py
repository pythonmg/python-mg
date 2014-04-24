#!/usr/bin/env python
# coding: utf-8
from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from apps.decorators import RegisterValidMixin, LoginRequiredMixin

from .models import Member, Social
from .forms import MemberForm, SocialFormset


class RegisterView(LoginRequiredMixin, FormView):
    form_class = MemberForm
    second_form_class = SocialFormset
    template_name = 'membros/v2/register.html'

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
                context['formset'] = self.second_form_class(self.request.POST)
        else:
            context['formset'] = self.second_form_class()

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        if formset.is_valid():
            for form_social in formset.forms:
                if form_social.is_valid() and form_social.cleaned_data['url']:
                    social = form_social.save(commit=False)
                    social.member = self.object
                    social.save()

            return redirect('account')
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get(self, request, *args, **kwargs):
        if Member.objects.filter(user=self.request.user).exists():
            return redirect('account')
        return super(RegisterView, self).get(self, request, *args, **kwargs)


class AccountView(RegisterValidMixin, TemplateView):
    template_name = 'membros/v2/account.html'


def detalhe(request, id, template='membros/detalhe.html'):
    membro = get_object_or_404(Member, pk=id)
    return render(request, template, {'membro': membro})


def consultar_por_nome(request, template='membros/listagem.html'):
    name = request.GET.get('name', '')
    membros = Member.objects.filter(nome__icontains=name, aprovado=True)[:5]
    return render(request, template, {'membros': membros})
