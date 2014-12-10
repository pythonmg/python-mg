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

        try:
            photo = Photo.objects.get(member=member)
        except Photo.DoesNotExist:
            photo = Photo()
            photo.member = member
        if meetup_member.photo:
            photo.photo_link = meetup_member.photo.photo_link
            photo.highres_link = meetup_member.photo.highres_link
            photo.thumb_link = meetup_member.photo.thumb_link
            photo.save()

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
    link = models.URLField()

    objects = MemberManager()

    def __unicode__(self):
        return self.name

    def photo_profile(self):
        try:
            photo = Photo.objects.get(member=self)
            if photo.thumb_link:
                return photo.thumb_link
            elif photo.highres_link:
                return photo.highres_link
            elif photo.photo_link:
                return photo.photo_link
        except Photo.DoesNotExist:
            pass
        return 'http://default_link'


class Social(models.Model):
    member = models.ForeignKey('meetup.Member', related_name='other_services')
    name = models.CharField(max_length=150)
    identifier = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return '{0}:{1}'.format(self.name, self.identifier)


class Photo(models.Model):
    member = models.OneToOneField('meetup.Member')
    photo_link = models.URLField(blank=True, null=True)
    highres_link = models.URLField(blank=True, null=True)
    thumb_link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.member.name
