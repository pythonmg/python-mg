# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

from django_gravatar.helpers import get_gravatar_url


class Member(models.Model):
    user = models.OneToOneField(User, primary_key=True,
                                related_name="member_profile")
    website = models.URLField(blank=True, null=True)
    enterprise = models.CharField(max_length=180, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    @property
    def avatar(self):
        import pdb; pdb.set_trace()
        url = get_gravatar_url(self.user.email, size=80)
        return url


class TypeSocial(models.Model):
    name = models.CharField(max_length=30)
    icon = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class Social(models.Model):
    url = models.URLField()
    type_social = models.ForeignKey(TypeSocial, related_name="social_list")
    member = models.ForeignKey(Member, related_name="social_list")

    def __unicode__(self):
        return u'%s %s' % (self.member.user.first_name, self.url)
