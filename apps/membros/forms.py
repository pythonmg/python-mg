#!/usr/bin/env python
from django import forms
from django.forms.models import inlineformset_factory

from .models import Member, Social, TypeSocial


class MemberForm(forms.ModelForm):
    website = forms.URLField(label=u'web', required=False)
    enterprise = forms.CharField(label=u'Empresa', required=False)

    class Meta:
        model = Member
        fields = ['website', 'enterprise']


class SocialForm(forms.ModelForm):
    TYPE_SOCIAL_CHOICES = [(x.id, x.name) for x in TypeSocial.objects.all()]

    url = forms.URLField(label=u'URL', required=False)
    """
    type_social = forms.CharField(
        label=u'Tipo da rede social',
        required=False,
        choices=TYPE_SOCIAL_CHOICES,
    )"""

    class Meta:
        model = Social
        fields = ['url', 'type_social']


SocialFormset = inlineformset_factory(
    Member, Social,
    form=SocialForm,
    fields=('url', 'type_social',),
    can_delete=True,
)
