from django.core.management.base import BaseCommand

from meetup.models import Member
from meetup.client import Meetup

meetup = Meetup()


class Command(BaseCommand):
    help = 'Create/Update members and users using MeetupAPI'

    def handle(self, *args, **options):
        new_members = 0
        members = meetup.members()

        for meetup_member in members:
            member, created = Member.objects.create_or_update(meetup_member)

            if created:
                new_members += 1

        self.stdout.write('Successfully create "%s" new members' % new_members)
