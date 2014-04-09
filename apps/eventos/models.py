# coding:utf-8

from django.db import models


class Evento(models.Model):
    titulo = models.CharField(max_length=255, verbose_name=u'Título')
    email = models.CharField(
        max_length=255, verbose_name=u'E-mail para contato')
    endereco = models.TextField(
        verbose_name=u'Endereço', blank=True, null=True)
    info = models.TextField(
        verbose_name=u'Informações adicionais', blank=True, null=True)
    data = models.DateTimeField(null=True, blank=True)
    preco = models.DecimalField(
        verbose_name=u'Preço', decimal_places=2,
        max_digits=10, default=0.0,
    )
    site = models.URLField(max_length=255, blank=True, null=True)
    imagem = models.ImageField(
        upload_to='eventos/',
        default='',
        blank=True)

    class Meta:
        ordering = ['-data']
        verbose_name_plural = u'Eventos'

    def __unicode__(self):
        return self.titulo
