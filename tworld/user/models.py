#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import ugettext_lazy as _
import logging

log = logging.getLogger(__name__)


class User(AbstractUser):
    def __unicode__(self):
        return self.username
