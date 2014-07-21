from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from django.core.urlresolvers import reverse_lazy

from core.mixins import LoginRequiredMixin
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostCreateView, self).form_valid(form)


class PostListView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'
