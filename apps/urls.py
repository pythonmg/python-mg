from django.conf.urls import patterns, include, url

# from .views import LoginView

urlpatterns = patterns(
    '',
    url(r'^$', 'apps.views.home', name='home'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'},
        name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^noticias/', include('apps.noticias.urls')),
    url(r'^membros/', include('apps.membros.urls')),
    url(r'^eventos/', include('apps.eventos.urls')),
    url(r'^projetos/', include('apps.projetos.urls')),
    url(r'^contribuicoes/', include('apps.contribuicoes.urls')),
)
