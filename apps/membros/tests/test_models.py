#!/usr/bin/env python
from django.test import TestCase

from model_mommy import mommy

from apps.membros.models import Member, Social


class MemberModelTest(TestCase):
    """
    classe responsavel por testar model Member
    """

    def setUp(self):
        """
        prepara testes para iniciar
        """
        self.member = mommy.make(Member)

    def test_return_unicode_method(self):
        """
        devera retornar o nome completo do membro
        """
        self.assertEqual(
            self.member.__unicode__(),
            u'%s %s' % (
                self.member.user.first_name,
                self.member.user.last_name
            )
        )


class SocialModelTest(TestCase):
    """
    classe responsavel por testar model Social
    """

    def setUp(self):
        """
        prepara testes para iniciar
        """
        self.social = mommy.make(Social)

    def test_return_unicode_method(self):
        """
        devera retornar o tipo de rede social
        """
        self.assertTrue(
            self.social.__unicode__(),
            u'%s' % self.social.type_social
        )
