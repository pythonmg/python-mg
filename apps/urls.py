from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^', include('apps.noticias.urls')),
    url(r'^participantes/', include('apps.participantes.urls')),
)