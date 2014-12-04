from django.core.management.base import BaseCommand, CommandError

from twitter_app.models import *

import time
from django.conf import settings

from twython import Twython

twitter = Twython(settings.TWITTER_APP_KEY, settings.TWITTER_APP_SECRET,
          settings.TWITTER_OAUTH_TOKEN, settings.TWITTER_OAUTH_TOKEN_SECRET)

from django.utils.html import urlize

import re

class Command(BaseCommand):
    help = 'Import tweets from hashtags and profiles'

    def handle(self, *args, **options):


        twitter_hashtags = TwitterHashtag.objects.all()
        twitter_users = TwitterUser.objects.all()

        n_tweets = 0

        for user in twitter_users:
            print user.name
            user_timeline= twitter.get_user_timeline(screen_name=user.name,count=20)

            for tweet in user_timeline:
                guid = tweet['id']

                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                text = urlize(tweet['text'])

                try:
                    tweet_obj = Tweet.objects.get(guid=guid)
                except Tweet.DoesNotExist:
                    tweet_obj = Tweet.objects.create(
                        guid=guid,
                        text=text,
                        created_at=ts,
                        )
                    tweet_obj.save()
                    n_tweets += 1


        for hashtag in twitter_hashtags:
            print hashtag.name
            result = twitter.search(q=hashtag.name,count=20)

            tweets = result['statuses']
    
            for tweet in tweets:
                guid = tweet['id']

                ts = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                text = urlize(tweet['text'])

                try:
                    tweet_obj = Tweet.objects.get(guid=guid)
                except Tweet.DoesNotExist:
                    tweet_obj = Tweet.objects.create(
                        guid=guid,
                        text=text,
                        created_at=ts,
                        )
                    tweet_obj.save()
                    n_tweets += 1

        self.stdout.write('Successfully imported "%s" tweets ' % n_tweets)