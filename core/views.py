from django.views.generic.list import ListView

from feeds.models import FeedItem


class Homepage(ListView):
    template_name = 'core/homepage.html'
    paginate_by = 5

    def get_queryset(self):
        return FeedItem.objects.exclude(
            feed__title='Github'
        ).order_by('-date_modified')
