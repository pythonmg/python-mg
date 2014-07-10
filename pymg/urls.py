from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('core.urls', namespace='core')),
    url(r'^social/', include('social.apps.django_app.urls',
        namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)
