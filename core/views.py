from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import CreateUserForm
# from .mixins import LoginRequiredMixin


class HomepageView(TemplateView):
    template_name = 'core/homepage.html'


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'core/register.html'
    success_url = '/'
