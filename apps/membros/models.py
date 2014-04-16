# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Social(models.Model):
    url = models.URLField()
    type_social = models.CharField(max_length=30)

    def __unicode__(self):
        return self.type_social


class Member(models.Model):
    user = models.OneToOneField(User, primary_key=True,
                                related_name="member_profile")
    website = models.URLField(blank=True, null=True)
    enterprise = models.CharField(max_length=180, blank=True, null=True)
    social = models.ManyToManyField(Social, null=True)

    def __unicode__(self):
        return self.user.first_name