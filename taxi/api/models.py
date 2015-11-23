# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


class LocationManager(models.Manager):
    def nearby(self, latitude, longitude, proximity):
        """
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
        # Great circle distance formula
        gcd = '''
            6371 * acos(
            cos(radians(%s)) * cos(radians(lat))
            * cos(radians(lon) - radians(%s)) +
            sin(radians(%s)) * sin(radians(lat))
            )
        '''
        gcd_lt = "{} < %s".format(gcd)
        return (
            self.get_queryset()
            .exclude(lat=None)
            .exclude(lon=None)
            .extra(
                select={'distance': gcd},
                select_params=[latitude, longitude, latitude],
                where=[gcd_lt],
                params=[latitude, longitude, latitude, proximity],
                order_by=['distance']
            )
        )


@python_2_unicode_compatible
class Driver(models.Model):
    '''
    Taxi driver
    '''
    lat = models.FloatField(_('Latitude'))
    lon = models.FloatField(_('Longitude'))
    is_ready = models.BooleanField(
        _('Ready for work'), default=True, db_index=True)

    objects = LocationManager()

    def __str__(self):
        return '%s' % self.pk

    class Meta:
        verbose_name = _('Driver')
        verbose_name_plural = _('Drivers')
        ordering = ('-is_ready', )


@python_2_unicode_compatible
class Order(models.Model):
    '''
    Taxi client order
    '''
    client = models.PositiveIntegerField(_('Client ID'))
    lat = models.FloatField(_('Latitude'))
    lon = models.FloatField(_('Longitude'))
    time = models.DateTimeField(_('Time for start'), db_index=True)
    is_closed = models.BooleanField(
        _('Finished'), default=False, db_index=True)

    def __str__(self):
        return '%s' % self.pk

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ('-is_closed', )
