# coding: utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext

from .noticias.models import Noticia
from .participantes.models import Participante


def home(request, template='index.html'):
    return render_to_response(
        template,
        {'noticias': Noticia.objects.order_by('-data')[:5]},
        context_instance=RequestContext(request),
    )