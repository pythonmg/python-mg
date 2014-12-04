from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from blog.models import Post

from .forms import CreateUserForm
# from .mixins import LoginRequiredMixin
from feeds.models import FeedItem
from twitter_app.models import Tweet

class HomepageView(ListView):
    template_name = 'core/homepage.html'
    # queryset = Post.objects.filter(status='PU').order_by('-created')
    queryset = FeedItem.objects.filter().order_by('-date_modified')

    paginate_by = 12


    

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        tweets = Tweet.objects.filter().order_by('-created_at')[:5]
        context['tweets'] = tweets
        return context
    


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = 'core/register.html'
    success_url = '/'
