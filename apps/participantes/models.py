# coding: utf-8

from django.db import models


class Participante(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=75)
    foto = models.ImageField(upload_to='participantes/')
    aprovado = models.BooleanField(default=False)

    cadastrado = models.DateTimeField(auto_now_add=True, editable=False) 

    class Meta:
        ordering = ['-cadastrado']

    def __unicode__(self):
        return self.nome