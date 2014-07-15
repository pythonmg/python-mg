from django.conf.urls import patterns, url

from .views import HomepageView, CreateUserView

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^register/$', CreateUserView.as_view(), name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'core/homepage.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
)
