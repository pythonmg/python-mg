from django.contrib import admin

from twitter_app.models import *

# Register your models here.
admin.site.register(TwitterHashtag)
admin.site.register(TwitterUser)
admin.site.register(Tweet)

