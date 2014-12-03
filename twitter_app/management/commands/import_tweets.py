from django.core.management.base import BaseCommand, CommandError

from twitter_app.models import *


import pprint
pp = pprint.PrettyPrinter(indent=4)
#date
from time import mktime
from datetime import datetime
from django.utils.html import strip_tags

from django.conf import settings
# import twitter
# from twitter import *
import tweepy


class Command(BaseCommand):
    help = 'Import tweets from hashtags and profiles'

    def handle(self, *args, **options):
        twitter_hashtags = TwitterHashtag.objects.all()
        twitter_users = TwitterUser.objects.all()

        #python-twitter
        # api = twitter.Api(consumer_key=settings.TWITTER_APP_KEY,
        #               consumer_secret=settings.TWITTER_APP_SECRET,
        #               access_token_key=settings.TWITTER_OAUTH_TOKEN,
        #               access_token_secret=settings.TWITTER_OAUTH_TOKEN_SECRET)

        # tweets = api.GetSearch('pugmg')
        # print [t.text for t in tweets]

        #twitter
        # auth = OAuth(
        #     consumer_key=settings.TWITTER_APP_KEY,
        #     consumer_secret=settings.TWITTER_APP_SECRET,
        #     token=settings.TWITTER_OAUTH_TOKEN,
        #     token_secret=settings.TWITTER_OAUTH_TOKEN_SECRET
        # )
        # t = Twitter(auth)
        # x = t.search.tweets(q="#pycon")

        
        ###tweepy

        auth = tweepy.OAuthHandler(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET)
        auth.set_access_token(settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)

        api = tweepy.API(auth)
        # public_tweets = api.home_timeline()
        result = api.search(q='pythonmg')
        for tweet in result:
            print tweet.text
        # for hashtag in hashtags:
        #     print 'hashtag %s' % (hashtag.name)
        #     statuses = api.GetSearch('pugmg')
        #     print dir(statuses)
            # print [s.text for s in statuses]


        # for profile in profiles:
        #     print 'profile %s' % (profile)
        #     statuses = api.GetUserTimeline(screen_name=profile.name)
        #     print [s.text for s in statuses]


        # n_feed_items = 0
        # for feed in feeds:
        #     print feed.title
        #     parsed = feedparser.parse(feed.feed_url)
        #     for entry in parsed.entries:
        #         print entry.title
        #         pp.pprint(entry)                
        #         #check if it's already in the database, if not create it
        #         guid = entry.id

        #         try:
        #             feed_item = FeedItem.objects.get(guid=guid)
        #         except FeedItem.DoesNotExist:
        #             feed_item = FeedItem.objects.create(
        #                 feed=feed,
        #                 title=entry.title,
        #                 link=entry.link,
        #                 summary=strip_tags(entry.summary),
        #                 guid=guid,
        #                 )

        #             #parse meetup, github and google groups
        #             if entry.link.startswith('http://www.meetup.com'):
        #                 #parse date
        #                 if 'published_parsed' in entry:
        #                     dt = datetime.fromtimestamp(mktime(entry['published_parsed']))
        #                     feed_item.date_modified = dt
                        
        #             if entry.link.startswith('https://github.com'):
        #                 feed_item.author = entry.author
        #                 if 'updated_parsed' in entry:
        #                     dt = datetime.fromtimestamp(mktime(entry['updated_parsed']))
        #                     feed_item.date_modified = dt
                        
                        
        #             if entry.link.startswith('https://groups.google.com'):
        #                 feed_item.author = entry.author
        #                 if 'published_parsed' in entry:
        #                     dt = datetime.fromtimestamp(mktime(entry['published_parsed']))
        #                     feed_item.date_modified = dt
                        
        #             # print 'before saving'
        #             # print feed_item, feed_item.date_modified
        #             feed_item.save()
        #             n_feed_items    += 1
        #         # poll.opened = False
        #         # poll.save()

        # self.stdout.write('Successfully imported "%s" feed items ' % n_feed_items)