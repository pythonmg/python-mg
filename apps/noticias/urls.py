from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.noticias.views',
    url(r'^(?P<id>\d+)/$', 'detalhe', name='noticia_detalhe'),
)
