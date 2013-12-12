# coding: utf-8

import string

from django.contrib import admin


def firstletterfilter(lookup_name):
    """
        Filtro pelo inicio de cada palavra, retorna para o template
        as iniciais que uma palavra pode começar e filtra pelo
        `lookup_name` que começa com a palavra.
    """
    class FirstLetterFilter(admin.SimpleListFilter):
        title = 'inicial'
        parameter_name = 'inicial'
        lookup_name = None

        def lookups(self, request, model_admin):
            iniciais = list(string.ascii_uppercase)
            return zip(iniciais, iniciais)

        def queryset(self, request, queryset):
            if self.value() is not None:
                return queryset.filter(**{
                    '%s__istartswith' % self.lookup_name: self.value()
                })
            return queryset

    FirstLetterFilter.lookup_name = lookup_name
    return FirstLetterFilter
