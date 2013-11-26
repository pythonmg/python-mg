from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.projetos.views',
    url(r'^(?P<id>\d+)/$', 'detalhe', name='projeto_detalhe'),
)