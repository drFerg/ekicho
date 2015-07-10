# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='icon',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='train',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
