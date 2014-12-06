from django.views.generic.list import ListView

from feeds.models import FeedItem


class Homepage(ListView):
    template_name = 'core/homepage.html'
    queryset = FeedItem.objects.filter().order_by('-date_modified')
    paginate_by = 9
