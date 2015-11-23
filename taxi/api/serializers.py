# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.utils import timezone

from rest_framework import serializers

from .models import Driver, Order
from .tasks import find_drivers


logger = logging.getLogger()


class DriverSerializer(serializers.ModelSerializer):
    '''
    Driver
    '''
    class Meta:
        model = Driver
        fields = (
            'id', 'lat', 'lon',
        )

    def update(self, instance, validated_data):
        instance = super(DriverSerializer, self).update(
            instance, validated_data)

        instance.is_ready = True
        logger.info('Driver %s is ready for work' % instance)

        return instance


class OrderSerializer(serializers.ModelSerializer):
    '''
    Order
    '''
    time = serializers.DateTimeField(required=False, default=timezone.now)

    class Meta:
        model = Order
        fields = (
            'id', 'client', 'time',
            'lat', 'lon',
        )

    def save(self, *args, **kwargs):
        res = super(OrderSerializer, self).save(*args, **kwargs)

        logger.info('Received new order')
        find_drivers.delay()

        return res
