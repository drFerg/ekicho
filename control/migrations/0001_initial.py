# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0002_auto_20150622_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='RollingStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('speed', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=3, choices=[(b'STP', b'Stopped'), (b'FWD', b'Forward'), (b'BWD', b'Backward'), (b'BRK', b'Braking')])),
                ('train', models.ForeignKey(to='trains.Train')),
            ],
        ),
    ]
