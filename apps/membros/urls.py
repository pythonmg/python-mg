from django.conf.urls import patterns, url


urlpatterns = patterns('apps.membros.views',
    url(r'^redirect/$', 'redirect_form', name='redirect_form'),
    url(r'^done/$', 'done', name='done'),
    url(r'^(?P<id>\d+)/$', 'detalhe', name='membro_detalhe'),
    url(r'^consultar/$', 'consultar_por_nome', name='membro_consultar'),
)