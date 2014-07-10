from django.views.generic.base import TemplateView

from .mixins import LoginRequiredMixin


class HomepageView(TemplateView):
    template_name = 'core/homepage.html'


class RevoceAccessView(LoginRequiredMixin, TemplateView):
    template_name = 'core/revoke.html'
