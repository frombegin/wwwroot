# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slide', '0002_slide_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.ImageField(height_field=b'height', upload_to=b'', width_field=b'width', verbose_name='\u56fe\u7247\u6587\u4ef6'),
        ),
    ]
