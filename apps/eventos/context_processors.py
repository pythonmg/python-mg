# coding: utf-8

from .models import Evento
from django.utils import timezone

def proximos_eventos(request):
	"""
		Irá aparecer na base.html o próximo evento,
		sempre no footer. Por isso foi criado um context_processors.
	"""
	eventos = Evento.objects.filter(data__gt=timezone.now())
	return {'eventos': eventos}