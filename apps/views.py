# coding: utf-8

from django.shortcuts import render
from django.template import RequestContext

from .noticias.models import Noticia
from .noticias.views import listagem


def home(request, template='index.html'):
    return listagem(request, template=template)