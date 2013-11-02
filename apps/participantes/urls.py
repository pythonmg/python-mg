from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.participantes.views.listagem', name='listagem_participantes'),
)