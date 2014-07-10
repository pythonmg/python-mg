from django.conf.urls import patterns, url

from .views import HomepageView, RevoceAccessView

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^revoke/$', RevoceAccessView.as_view(), name='revoke'),
)
