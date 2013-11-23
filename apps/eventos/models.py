# coding:utf-8

from django.db import models

EVENTO_CHOICE = (('E', 'Encontro'), ('P', 'Palestras'), ('C', 'CodeDojo'))

class Organizador(models.Model):
	nome = models.CharField(max_length=180)
	url = models.URLField(max_length=200)
	imagem = models.ImageField(upload_to='organizadores/', blank=True)

	class Meta:
		ordering = ['-nome']
		verbose_name_plural = u'Organizadores'

	def __unicode__(self):
		return self.nome

class Evento(models.Model):
	nome = models.CharField(max_length=200, verbose_name=u'Título')
	descricao = models.TextField(verbose_name=u'Descrição')
	data = models.DateTimeField()
	url = models.URLField(max_length=200)
	organizadores = models.ManyToManyField(Organizador)

	class Meta:
		ordering = ['-data']
		verbose_name_plural = u'Eventos'

	def __unicode__(self):
		return self.nome

class Programacao(models.Model):
	titulo = models.CharField(max_length=200, verbose_name=u'Título')
	descricao = models.TextField(verbose_name=u'Descrição')
	hora_inicio = models.TimeField(verbose_name=u'De')
	hora_fim = models.TimeField(verbose_name=u'a')
	evento = models.ForeignKey(Evento)

	class Meta:
		ordering = ['-evento', '-hora_inicio']
		verbose_name_plural = u'Programações'

	def __unicode__(self):
		return self.titulo