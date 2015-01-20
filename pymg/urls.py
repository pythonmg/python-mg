from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),

    # Flatpages
    url(r'^about/$',
        'django.contrib.flatpages.views.flatpage',
        {'url': '/about/'}, name='about'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
