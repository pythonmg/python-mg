from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from feeds.models import FeedItem

from .forms import ContactForm


class Homepage(ListView):
    template_name = 'core/homepage.html'
    paginate_by = 5

    def get_queryset(self):
        return FeedItem.objects.exclude(
            feed__title='Github'
        ).order_by('-date_modified')


class Contact(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_mail()
        return super(Contact, self).form_valid()
