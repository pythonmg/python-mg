from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.eventos.views',
    url(r'^(?P<id>\d+)/$', 'detalhe', name='evento_detalhe'),
)
