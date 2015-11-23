# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .models import Driver, Order
from .serializers import DriverSerializer, OrderSerializer


class DriverViewSet(viewsets.ModelViewSet):
    '''
    Driver
    '''
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    http_method_names = ['put', ]

    def get_object(self):
        '''
        Create if not exists
        '''
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {
            self.lookup_field: int(self.kwargs[lookup_url_kwarg]),
            'defaults': dict(lat=0, lon=0),
        }

        obj, created = queryset.get_or_create(**filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj


class OrderViewSet(viewsets.ModelViewSet):
    '''
    Order
    '''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    http_method_names = ['post', 'delete', ]
