from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from blog.models import Post
from .forms import CreateUserForm
# from .mixins import LoginRequiredMixin


class HomepageView(ListView):
    template_name = 'core/homepage.html'
    queryset = Post.objects.filter(status='PU').order_by('-created')
    paginate_by = 4


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'core/register.html'
    success_url = '/'
