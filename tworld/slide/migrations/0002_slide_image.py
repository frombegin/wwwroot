# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.ImageField(default=None, upload_to=b'', verbose_name='\u56fe\u7247\u6587\u4ef6'),
            preserve_default=False,
        ),
    ]
