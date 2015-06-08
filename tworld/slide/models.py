#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import auth
from django.conf import settings
# Create your models here.


class Slide(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)  #auth.get_user_model())
    name = models.CharField(max_length=100)
    image = models.ImageField(u'图片文件', width_field='width', height_field='height')
    width = models.IntegerField()
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)



    def __unicode__(self):
        return u"name: %s, %d" % (self.name, self.user_id)