from django import forms
from .models import Participante

class ParticipanteForm(forms.ModelForm):
	class Meta:
		model = Participante