#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tworld.portal import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'tworld.portal.views.index', name='user.home'),
]
