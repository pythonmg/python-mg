# -*- coding:utf-8 -*-

#Core Django imports
from django.test import TestCase
from django.utils import timezone

#Third-party app imports
from model_mommy import mommy

# Relative imports of the 'app-name' package


######### WHAT WE NEED TEST #########
#
# 1 - creating / criação
# 2 - reading / leitura
# 3 - updating / atualização
# 4 - deleting / deleção
# 5 - model methods / metodos do model
# 6 - model managers / não ha tradução para isto
# 7 - model managers methods / não ha tradução para isto

############# TIPS ##################
#
# 1 - Cada função de test deve haver apenas 1 assert
#
#####################################

class ModelNameTests(TestCase):
    """
    """
