# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Driver, Order


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('pk', 'is_ready', 'lat', 'lon', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'is_closed', 'time', 'lat', 'lon', )
