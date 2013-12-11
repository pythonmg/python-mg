# coding: utf-8

"""
    Social: context processor que será responsável por retornar os dados
    sobre redes sociais da Python-MG

    ZenPython: responsável por retornar um dos mandamentos do python de forma
    random que será exibido no footer da página.
"""


import random


def social(request):
    return {
        'email_url': 'mailto:python.minas.gerais@gmail.com',
        'twitter_url': 'https://twitter.com/pythonmg',
        'github_url': 'https://github.com/python-mg',
        'google_url': 'https://plus.google.com/communities/113572164757551993822',
        'googlegroups_url': 'https://groups.google.com/forum/?fromgroups#!forum/python-mg',
    }


def zen_python(request):

    zen = """
        Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it's a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let's do more of those!
    """
    frases = [frase for frase in zen.split('\n') if frase.strip()]

    random.shuffle(frases)

    return {
        'zen_python': frases[0]
    }
