from django.conf.urls import patterns, url

from .views import Homepage

urlpatterns = patterns(
    '',
    url(r'^$', Homepage.as_view(), name='homepage'),
)
