from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from blog.models import Post
from .forms import CreateUserForm
# from .mixins import LoginRequiredMixin
from feeds.models import FeedItem

class HomepageView(ListView):
    template_name = 'feeds/feeds.html'
    # queryset = Post.objects.filter(status='PU').order_by('-created')
    queryset = FeedItem.objects.filter().order_by('-date_modified')
    
    paginate_by = 12


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'core/register.html'
    success_url = '/'
