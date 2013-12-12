from django.forms import ModelForm
from .models import Membro


class MembroForm(ModelForm):
    class Meta:
        model = Membro
        fields = ['nome','data_nascimento', 'genero',
                    'email', 'url', 'foto', 'descricao']