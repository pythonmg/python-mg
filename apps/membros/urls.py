from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.membros.views',
    url(r'^register/stage2/$', 'register_final', name='register-final'),
    url(r'^done/$', 'done', name='done'),
    url(r'^(?P<id>\d+)/$', 'detalhe', name='membro_detalhe'),
    url(r'^consultar/$', 'consultar_por_nome', name='membro_consultar'),
)
