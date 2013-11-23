from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.eventos.views',
	url(r'^(?P<id>\d+)/$', 'detalhe', name='evento_detalhe'),
)