# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import *

urlpatterns = [

    url(r'^$', UserCreate.as_view(), name='create-user'),

    ]