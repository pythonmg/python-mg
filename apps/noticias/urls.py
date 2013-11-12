from django.conf.urls import patterns, url


urlpatterns = patterns('apps.noticias.views',
    #url(r'^$', 'apps.noticias.views.listagem', name='listagem_noticias'),
    url(r'^(?P<id>\d+)/$', 'detalhe', name='noticia_detalhe'),
)
