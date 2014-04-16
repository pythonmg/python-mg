# -*- coding:utf-8 -*-

#Core Django imports
from django.test import TestCase
from django.utils import timezone

#Third-party app imports
from model_mommy import mommy

# Relative imports of the 'app-name' package
from apps.contribuicoes.models import Contribuicoes
from apps.contribuicoes.forms import ContribuicaoForm

# ######## WHAT WE NEED TEST #########
#
# 1 - form methods / metodos no formulario
# 2 - clean() methods / metodos clean() no form
# 3 - custom fields / campos customizados e widgets

# ############ TIPS ##################
#
# 1 - Cada função de test deve haver apenas 1 assert
#
# ####################################


class ContribuicoesFormTests(TestCase):
    """
    Classe para teste do formulario de contribuicoes
    """

    def setUp(self):
        """
        Inicializa os testes
        """
        self.contribuicao = mommy.make(Contribuicoes)

    def test_valid_form(self):
        """
        Testa se o formulario de contribuicao é válido
        """

        dados = {
            'titulo': self.contribuicao.titulo,
            'descricao': self.contribuicao.descricao,
        }

        form = ContribuicaoForm(data=dados)

        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Testa se o formulario de contribuicao é inválido
        """
        self.contribuicao.titulo = None
        dados = {
            'titulo': self.contribuicao.titulo,
            'descricao': self.contribuicao.descricao,
        }

        form = ContribuicaoForm(data=dados)

        self.assertFalse(form.is_valid())

    def test_required_field_titulo_form(self):
        """
        Testa se o campo titulo é obrigatório
        """
        self.contribuicao.titulo = None
        dados = {
            'titulo': self.contribuicao.titulo,
            'descricao': self.contribuicao.descricao,
        }

        form = ContribuicaoForm(data=dados)
        self.assertIn(u'Este campo é obrigatório.', form.errors['titulo'])

    def test_required_field_descricao_form(self):
        """
        Testa se o campo descricao é obrigatório
        """
        self.contribuicao.descricao = None
        dados = {
            'titulo': self.contribuicao.titulo,
            'descricao': self.contribuicao.descricao,
        }

        form = ContribuicaoForm(data=dados)
        self.assertIn(u'Este campo é obrigatório.', form.errors['descricao'])
