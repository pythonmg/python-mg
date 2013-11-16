# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

CHOICES_SEXO = (('M', 'Masculino'), ('F', 'Feminino'))

class Membro(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=75)
    url = models.URLField(max_length=200)
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

    def save(self):
        if self.user == None and self.aprovado:
            senha = User.objects.make_random_password(length=10)
            u = User.objects.create_user(self.email, self.email, senha)
            u.save()
            self.user = u
        else:
            u = User.objects.get(email=self.email)
            #if u:
            #    raise ValidationError
        super(Membro, self).save()