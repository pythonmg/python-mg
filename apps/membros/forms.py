from django.forms import ModelForm
from .models import Member


class MembroForm(ModelForm):
    class Meta:
        model = Member
        fields = ['website', 'enterprise']
