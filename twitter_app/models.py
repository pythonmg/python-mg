from django.db import models

class TwitterHashtag(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

class TwitterUser(models.Model):
    name = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

# class Tweet()