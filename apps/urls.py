from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'apps.home.views.home', name="home"),
	url(r'^noticias/', include('apps.noticias.urls')),
    url(r'^participantes/', include('apps.participantes.urls')),
)