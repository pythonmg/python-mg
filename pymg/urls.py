from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'', include('core.urls', namespace='core')),
    url(r'^post/', include('blog.urls', namespace='blog')),
    url(r'^social/', include('social.apps.django_app.urls',
        namespace='social')),
    (r'^comments/', include('django_comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
