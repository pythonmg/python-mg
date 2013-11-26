from django.db import models

# Create your models here.
class Projeto(models.Model):
	nome = models.CharField(max_length=180)
	descricao = models.TextField()
	url = models.URLField()
	criado = models.DateField()
	atualizado = models.DateTimeField(auto_now_add=True, editable=False)

	class Meta:
		ordering = ['atualizado', '-criado']

	def __unicode__(self):
		return self.nome