from django.db import models
from django.utils.text import slugify
from datetime import datetime


class Post(models.Model):
    STATUS_CHOICES = (
        ('DR', 'Draft'),
        ('PU', 'Publish')
    )

    title = models.CharField(verbose_name='Title', max_length=180)
    slug = models.SlugField(verbose_name='Slug', max_length=210)
    body = models.TextField(verbose_name='Body')
    created = models.DateTimeField(verbose_name='Created')
    updated_on = models.DateTimeField(verbose_name='Updated on')
    status = models.CharField(verbose_name='Status', max_length=2,
                              choices=STATUS_CHOICES, default='DR')
    author = models.ForeignKey('auth.User', verbose_name='Author')

    def __unicode__(self):
        return unicode(self.title)

    def save(self):
        if not self.created:
            self.created = datetime.now()
        self.slug = slugify(self.title)
        self.updated_on = datetime.now()
        return super(Post, self).save()
