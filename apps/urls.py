from django.conf.urls import patterns, include, url

# from .views import LoginView

urlpatterns = patterns(
    'apps.views',
    url(r'^$', 'home', name='home'),
    url(r'^logout/$', 'logout', name='logout'),

    url(r'^noticias/', include('apps.noticias.urls')),
    url(r'^membros/', include('apps.membros.urls')),
    url(r'^eventos/', include('apps.eventos.urls')),
    url(r'^projetos/', include('apps.projetos.urls')),
    url(r'^contribuicoes/', include('apps.contribuicoes.urls')),
)
