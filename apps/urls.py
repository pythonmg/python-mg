from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'apps.views.home', name="home"),
	url(r'^noticias/', include('apps.noticias.urls')),
    url(r'^membros/', include('apps.membros.urls')),
    url(r'^eventos/', include('apps.eventos.urls')),
    url(r'^projetos/', include('apps.projetos.urls')),
)