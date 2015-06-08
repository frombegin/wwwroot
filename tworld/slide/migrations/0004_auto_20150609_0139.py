# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0003_auto_20150609_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='height',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slide',
            name='width',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
