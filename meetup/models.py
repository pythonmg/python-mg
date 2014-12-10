from django.db import models


class MemberManager(models.Manager):

    def create_or_update(self, meetup_member):
        try:
            member = self.get(guid=meetup_member.guid)
            created = False
        except Member.DoesNotExist:
            member = Member()
            member.guid = meetup_member.guid
            created = True
        member.name = meetup_member.name
        member.link = meetup_member.link

        member.save()

        if member.photo and meetup_member.photo:
            member.photo.delete()
        elif not member.photo and meetup_member.photo:
            member.photo = Photo()

        if meetup_member.photo:
            member.photo.photo_link = meetup_member.photo.photo_link
            member.photo.highres_link = meetup_member.photo.highres_link
            member.photo.thumb_link = meetup_member.photo.thumb_link
            member.photo.save()

        for meetup_social in meetup_member.social:
            try:
                social = member.other_services.get(name=meetup_social.name)
            except Social.DoesNotExist:
                social = Social()
            social.member = member
            social.name = meetup_social.name
            social.identifier = meetup_social.identifier
            social.save()

        return member, created


class Member(models.Model):
    guid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    photo = models.OneToOneField('meetup.Photo', null=True)
    link = models.URLField()

    objects = MemberManager()

    def __unicode__(self):
        return self.name


class Social(models.Model):
    member = models.ForeignKey('meetup.Member', related_name='other_services')
    name = models.CharField(max_length=150)
    identifier = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return '{0}:{1}'.format(self.name, self.identifier)


class Photo(models.Model):
    photo_link = models.URLField(blank=True, null=True)
    highres_link = models.URLField(blank=True, null=True)
    thumb_link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.guid
