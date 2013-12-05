# coding: utf-8

from django.db import models
from django.conf import settings


class Noticia(models.Model):
    titulo = models.CharField(verbose_name=u'Título', max_length=150)
    conteudo = models.TextField(verbose_name=u'Conteúdo')

    data = models.DateTimeField(auto_now_add=True, editable=False)
    visualizacoes = models.IntegerField(verbose_name=u'Visualizações', default=0, editable=False)
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    

    class Meta:
        ordering = ['-data']

    def __unicode__(self):
        return self.titulo
