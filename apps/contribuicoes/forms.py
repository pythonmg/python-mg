# -*- coding:utf-8 -*-

# Stdlib imports

# Core Django imports
from django.forms import ModelForm

# Third-party app imports

# Imports from your apps
from .models import Contribuicoes


class ContribuicaoForm(ModelForm):
    """Cria um form baseado no model de contribuicoes"""
    class Meta:
        model = Contribuicoes
        fields = ['titulo', 'descricao']
