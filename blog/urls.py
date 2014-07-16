from django.conf.urls import patterns, url

from .views import PostCreateView, PostListView, PostDetailView

urlpatterns = patterns(
    '',
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^list/$', PostListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='detail')
)
