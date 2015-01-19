from django.db import models


class MemberManager(models.Manager):

    def create_or_update(self, meetup_member):
        member, created = self.get_or_create(guid=meetup_member.guid)
        member.name = meetup_member.name
        member.link = meetup_member.link
        member.save()

        photo, _ = Photo.objects.get_or_create(member=member)

        if meetup_member.photo:
            photo.photo_link = meetup_member.photo.photo_link
            photo.highres_link = meetup_member.photo.highres_link
            photo.thumb_link = meetup_member.photo.thumb_link
            photo.save()

        for meetup_social in meetup_member.social:
            social, _ = member.other_services.get_or_create(name=meetup_social.name)
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
            if photo.default_link:
                return photo.default_link
        except Photo.DoesNotExist:
            pass
        return '/static/img/user-default.jpg'


class Social(models.Model):
    member = models.ForeignKey('meetup.Member', related_name='other_services')
    name = models.CharField(max_length=150)
    identifier = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return '{}:{}'.format(self.name, self.identifier)


class Photo(models.Model):
    member = models.OneToOneField('meetup.Member')
    photo_link = models.URLField(blank=True, null=True)
    highres_link = models.URLField(blank=True, null=True)
    thumb_link = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.member.name

    @property
    def default_link(self):
        available_links = self.get_avaiable_links()
        if available_links:
            return available_links[0]
        return

    def get_avaiable_links(self):
        links = ['photo_link', 'highres_link', 'thumb_link']
        return filter(lambda link: getattr(self, link, None), links)
