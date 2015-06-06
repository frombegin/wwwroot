#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")
