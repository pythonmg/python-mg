from django.conf.urls import patterns, url


urlpatterns = patterns('apps.membros.views',
    url(r'^cadastrar/$', 'cadastrar', name='membro_cadastro'),
    url(r'^(?P<id>\d+)/$', 'detalhe', name='membro_detalhe'),
    url(r'^(?P<name>\w+)/$', 'consultar_por_nome', name='membro_consultar'),
)