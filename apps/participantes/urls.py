from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^cadastrar/$', 'apps.participantes.views.cadastrar', name='participante_cadastro'),
    url(r'^(?P<id>\d+)/$', 'apps.participantes.views.detalhe', name='participante_detalhe'),
    url(r'^$', 'apps.participantes.views.listagem', name='participante_listagem'),
)