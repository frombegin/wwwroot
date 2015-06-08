#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from django.contrib.auth import models
from django.db import models
# from django.utils.translation import ugettext_lazy as _
import logging

log = logging.getLogger(__name__)


class Profile(models.Model):
    def __unicode__(self):
        return self.username
