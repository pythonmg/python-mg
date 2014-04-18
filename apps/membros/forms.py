#!/usr/bin/env python
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from .models import Member, Social


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['website', 'enterprise']


SocialFormset = inlineformset_factory(
    Member, Social,
    fields=('url', 'type_social',),
    can_delete=True,
)
