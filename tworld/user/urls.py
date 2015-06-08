#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from tworld.user import views

urlpatterns = [
    url(r'^$', 'tworld.user.views.index', name='user.home'),

    # URL pattern for the UserListView
    # url(regex=r'^$', view=views.UserListView.as_view(), name='list'),

    # # URL pattern for the UserRedirectView
    # url(regex=r'^~redirect/$', view=views.UserRedirectView.as_view(), name='user.redirect'),
    #
    # # URL pattern for the UserDetailView
    # url(regex=r'^(?P<username>[\w.@+-]+)/$', view=views.UserDetailView.as_view(), name='user.detail'),
    #
    # # URL pattern for the UserUpdateView
    # url(regex=r'^~update/$', view=views.UserUpdateView.as_view(), name='user.update'),
]