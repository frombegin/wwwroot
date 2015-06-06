#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'tworld.user.views.index', name='user.home'),
]