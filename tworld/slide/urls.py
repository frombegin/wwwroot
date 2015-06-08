#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tworld.slide import views

from tworld.slide import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'tworld.slide.views.index', name='slide.home'),
    url(r'^list/$', views.SlideList.as_view(), name='slide.list'),
]
