from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.views.home', name='home'),
    url(r'^login/$', 'apps.views.login', name='login'),
    url(r'^logout/$', 'apps.views.logout', name='logout'),

    url(r'^noticias/', include('apps.noticias.urls')),
    url(r'^membros/', include('apps.membros.urls')),
    url(r'^eventos/', include('apps.eventos.urls')),
    url(r'^projetos/', include('apps.projetos.urls')),
)
