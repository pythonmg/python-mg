# coding: utf-8

from django.contrib import admin

from apps.common.decorators import attr_decorator
from apps.common.admin import firstletterfilter

from .models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'info', 'data', 'show_url')
    date_hierarchy = 'data'
    list_filter = ('data', firstletterfilter('titulo'))
    search_fields = ('titulo', 'info', 'site')

    @attr_decorator(
        short_description='url', allow_tags=True, admin_order_field='site')
    def show_url(self, obj):
        return '<a target="_blank" href="{0}">{0}</a>'.format(obj.site)

admin.site.register(Evento, EventoAdmin)
