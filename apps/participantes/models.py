# coding: utf-8
from django.db import models

class Participante(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=75)
    url = models.URLField(max_length=200)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='participantes/', default='participantes/avatar.gif')
    descricao = models.TextField(max_length=255)
    aprovado = models.BooleanField(default=False)

    cadastrado = models.DateTimeField(auto_now_add=True, editable=False) 

    class Meta:
        ordering = ['-cadastrado']

    def __unicode__(self):
        return self.nome