from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages.views import flatpage

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),

    # Flatpages
    url(r'^about/$', flatpage, {'url': '/about/'}, name='about'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
