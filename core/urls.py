from django.conf.urls import patterns, url

from .views import Homepage, Contact

urlpatterns = [
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
]
