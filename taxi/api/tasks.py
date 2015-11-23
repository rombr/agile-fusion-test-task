# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.utils import timezone

from celery import task
from celery.task.schedules import crontab

from .models import Driver, Order


logger = logging.getLogger()


@task.periodic_task(run_every=crontab(minute='*/1'))
def find_drivers():
    '''
    Find drivers for clients
    '''
    logger.info('Find drivers starts')
    for order in Order.objects.filter(
            is_closed=False, time__lte=timezone.now()).order_by('time'):
        logger.info('Find driver for order %s' % order)

        nearest_driver = Driver.objects.nearby(
            order.lat, order.lon, 20).first()
        if not nearest_driver:
            logger.info('For order %s was not found driver in 20 km.' % (
                order, ))
            continue

        logger.info('For order %s was found driver %s' % (
            order, nearest_driver))

        order.is_closed = True
        order.save(update_fields=['is_closed'])

        nearest_driver.is_ready = False
        nearest_driver.save(update_fields=['is_ready'])

        logger.info(nearest_driver)
    logger.info('Find drivers ends')
