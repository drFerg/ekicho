# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_rollingstock_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='rollingstock',
            name='direction',
            field=models.IntegerField(default=2),
        ),
    ]
