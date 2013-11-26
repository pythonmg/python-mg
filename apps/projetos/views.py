from django.shortcuts import render, get_object_or_404

from .models import Projeto


def detalhe(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, 'projetos/detalhe.html', {'projeto': projeto})