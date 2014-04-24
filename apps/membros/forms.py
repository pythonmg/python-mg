#!/usr/bin/env python
from django import forms
from django.forms.models import inlineformset_factory

from .models import Member, Social, TypeSocial


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ['website', 'enterprise']


class SocialForm(forms.ModelForm):
    TYPE_CHOICES = [(x.id, x.name) for x in TypeSocial.objects.all()]

    url = forms.URLField(required=False)
    type_social = forms.ChoiceField(
        choices=TYPE_CHOICES, required=False)

    class Meta:
        model = Social
        fields = ['url', 'type_social']

    def clean(self):
        self._validade_unique = True
        id = self.cleaned_data.get('type_social')
        self.cleaned_data['type_social'] = TypeSocial.objects.get(pk=id)

        return self.cleaned_data


SocialFormset = inlineformset_factory(
    Member, Social,
    form=SocialForm,
    can_delete=False,
)
