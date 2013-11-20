# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save


CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))


class Membro(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=75, unique=True)
    url = models.URLField(max_length=200, null=True)
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=CHOICES_SEXO)
    foto = models.ImageField(upload_to='membros/', default='membros/avatar.gif')
    descricao = models.TextField(max_length=255)
    aprovado = models.BooleanField(default=False)

    cadastrado = models.DateTimeField(auto_now_add=True, editable=False)

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-cadastrado']

    def __unicode__(self):
        return self.nome


def update_user(sender, instance, **kwargs):
    from random import shuffle
    from string import letters, digits
    
    combination = list(letters + digits)
    shuffle(combination)
    senha = combination[:10]

    if instance.aprovado and not instance.user:
        user = User.objects.create(
            username=instance.email,
            email=instance.email,
            password=senha)
        user.set_password(senha)
        instance.user = user
        instance.save()

pre_save.connect(update_user, sender=Membro)
