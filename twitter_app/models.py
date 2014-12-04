from django.db import models

class TwitterHashtag(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class TwitterUser(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class Tweet(models.Model):
    guid = models.CharField(max_length=500, unique=True, db_index=True)
    text = models.TextField(blank=True)
    url = models.URLField(max_length=500)
    created_at = models.DateTimeField(blank=True, null=True)
    # date_modified = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return self.text
    

# [u'contributors', u'truncated', u'text', u'in_reply_to_status_id', u'id', u'favorite_count', u'source', u'retweeted', u'coordinates', u'entities', u'in_reply_to_screen_name', u'id_str', u'retweet_count', u'in_reply_to_user_id', u'favorited', u'user', u'geo', u'in_reply_to_user_id_str', u'possibly_sensitive', u'lang', u'created_at', u'in_reply_to_status_id_str', u'place']
