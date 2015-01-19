from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=500)
    feed_url = models.URLField(unique=True, max_length=500)
    public_url = models.URLField(max_length=500)

    def __unicode__(self):
        return self.title


class FeedItem(models.Model):
    feed = models.ForeignKey(Feed)
    author = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    link = models.URLField(max_length=500)
    summary = models.TextField(blank=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    guid = models.CharField(max_length=500, unique=True, db_index=True)

    class Meta:
        ordering = ("-date_modified",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.link
