# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from rest_framework import routers

from .views import DriverViewSet, OrderViewSet


# API routers
api_router = routers.DefaultRouter()
api_router.register(r'drivers', DriverViewSet)
api_router.register(r'orders', OrderViewSet)


urlpatterns = [
    url(r'^', include(api_router.urls)),
]
