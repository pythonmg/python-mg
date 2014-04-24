from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import AccountView, RegisterView


urlpatterns = patterns(
    'apps.membros.views',
    # url(r'^register/stage2/$', 'register', name='register'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^account/$', AccountView.as_view(), name='account'),
    url(r'^(?P<id>\d+)/$', 'detalhe', name='membro_detalhe'),
    url(r'^consultar/$', 'consultar_por_nome', name='membro_consultar'),
)
