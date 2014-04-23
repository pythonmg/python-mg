# coding:utf-8

from django.db import models

# Create your models here.


class Empresas(models.Model):
    nome = models.CharField(
        max_length=180,
        verbose_name=u'Nome')
    site = models.URLField(
        verbose_name=u'Site',
        blank=True,
        null=True)
    email = models.EmailField(max_length=75)
    endereco = models.CharField(max_length=180)
    cidade = models.CharField(max_length=200)
    cep = models.CharField(
        max_length=9,
        blank=True,
        null=True)
    imagem = models.ImageField(u"Imagem", upload_to=u"empresa/%Y/%m",
                               blank=True, null=True)
    disponivel = models.BooleanField(
        default=False,
        verbose_name=u'Disponível',
        help_text=u'Está disponível')
    interesse = models.BooleanField(
        default=False,
        verbose_name=u'Interesse',
        help_text=u'Possui interesse em alguma publicação')

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = u'Empresa'
        verbose_name_plural = u'Empresas'
