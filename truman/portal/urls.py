#!/usr/bin/env python
# -*- coding: utf-8 -*-

from truman.portal import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'truman.portal.views.index', name='user.home'),
]
