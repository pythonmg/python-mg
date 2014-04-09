# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ``created`` and ``modified``
    fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    """
    Atributo da classe TimeStampedModel para
    referenciar um campo de data de criação

    Caracteristicas:
    DateTimeField
    auto now add: True
    """

    modified = models.DateTimeField(auto_now=True)
    """
    Atributo da classe TimeStampedModel para
    referenciar um campo de data de modificado

    Caracteristicas:
    DateTimeField
    auto now: True
    """

    class Meta:
        """
        Seta a classe como abstrata
        """
        abstract = True
