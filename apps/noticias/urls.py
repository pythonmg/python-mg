from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	#url(r'^$', 'apps.noticias.views.listagem', name='listagem_noticias'),
    url(r'^(?P<id>\d+)/$', 'apps.noticias.views.detalhe', name='noticia_detalhe'),
)