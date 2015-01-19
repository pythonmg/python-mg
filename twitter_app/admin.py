from django.contrib import admin

from twitter_app.models import Tweet, TwitterUser, TwitterHashtag

admin.site.register(TwitterHashtag)
admin.site.register(TwitterUser)
admin.site.register(Tweet)
