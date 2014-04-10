#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

urlpatterns = patterns(
    'contributions.views',
    url(r'^$', 'contribuicao', name='contribuicao'),
)
