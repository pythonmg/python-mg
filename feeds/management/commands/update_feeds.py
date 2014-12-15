import pprint
import feedparser

from time import mktime
from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils.html import strip_tags

from feeds.models import Feed, FeedItem

pp = pprint.PrettyPrinter(indent=4)


class Command(BaseCommand):
    help = 'Update all feeds'

    def handle(self, *args, **options):
        feeds = Feed.objects.all()
        n_feed_items = 0

        for feed in feeds:
            print feed.title
            parsed = feedparser.parse(feed.feed_url)

            for entry in parsed.entries:
                print entry.title
                pp.pprint(entry)
                #check if it's already in the database, if not create it
                guid = entry.id

                try:
                    feed_item = FeedItem.objects.get(guid=guid)
                except FeedItem.DoesNotExist:
                    feed_item = FeedItem.objects.create(
                        feed=feed,
                        title=entry.title,
                        link=entry.link,
                        summary=strip_tags(entry.summary),
                        guid=guid,
                    )

                    #parse meetup, github and google groups
                    if entry.link.startswith('http://www.meetup.com'):
                        #parse date
                        if 'published_parsed' in entry:
                            dt = datetime.fromtimestamp(mktime(entry['published_parsed']))
                            feed_item.date_modified = dt

                    if entry.link.startswith('https://github.com'):
                        feed_item.author = entry.author
                        if 'updated_parsed' in entry:
                            dt = datetime.fromtimestamp(mktime(entry['updated_parsed']))
                            feed_item.date_modified = dt

                    if entry.link.startswith('https://groups.google.com'):
                        feed_item.author = entry.author
                        if 'published_parsed' in entry:
                            dt = datetime.fromtimestamp(mktime(entry['published_parsed']))
                            feed_item.date_modified = dt

                    feed_item.save()
                    n_feed_items += 1

        self.stdout.write('Successfully imported "%s" feed items ' % n_feed_items)
