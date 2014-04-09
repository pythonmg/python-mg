# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utils.translation import ugettext as _

# Relative imports

from common.models import TimeStampedModel


class Contribuicoes(TimeStampedModel):
    """
    Classe model de contribuicoes
    para guardar materiais (artigos, blogs) para serem
    aprovados pela comunidade python-mg
    """

    titulo = models.CharField(
        verbose_name=_(u'Titulo'),
        max_length=100
    )
    """
    Atributo da classe para
    referenciar um titulo da contribuicao

    Caracteristicas:
    Tipo: CharField
    Max Length: 100
    verbose name: Titulo
    """

    descricao = models.TextField(
        verbose_name=_(u'Descrição'),
    )
    """
    Atributo da classe para
    uma descrição da contribuição

    Caracteristicas:
    Tipo: TextField
    verbose name: Descrição
    """

    aprovado = models.BooleanField(
        verbose_name=_(u'Contribuição Aprovada?')
    )
    """
    Atributo da classe para
    setar se a contribuição foi aprovada ou nao

    Caracteristicas:
    Tipo: BooleanField
    verbose name: Contribuição Aprovada?
    """

    class Meta:
        """
        Seta a classe como abstrata
        """
        ordering = ['created']
        verbose_name = _(u'Contribuição')
        verbose_name_plural = _(u'Contribuições')

        def __unicode__(self):
            return u'%s' % (self.titulo)
