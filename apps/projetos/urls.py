from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.projetos.views',
    url(r'^(?P<id>\d+)/$', 'detalhe', name='projeto_detalhe'),
)
