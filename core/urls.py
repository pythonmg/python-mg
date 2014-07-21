from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

from .views import HomepageView, CreateUserView

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='home'),
    url(r'^register/$', CreateUserView.as_view(), name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'core/homepage.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
    url(r'^user/password/change/$',
        'django.contrib.auth.views.password_change',
        {
            'template_name': 'core/password_change.html',
            'post_change_redirect': reverse_lazy('core:home')
        }, name='password_change'),
)
