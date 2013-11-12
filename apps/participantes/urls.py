from django.conf.urls import patterns, url


urlpatterns = patterns('apps.participantes.views',
    url(r'^cadastrar/$', 'cadastrar', name='participante_cadastro'),
    url(r'^(?P<id>\d+)/$', 'detalhe', name='participante_detalhe'),
    url(r'^$', 'listagem', name='participante_listagem'),
)