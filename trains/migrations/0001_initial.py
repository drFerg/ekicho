# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'CMTR', max_length=4, choices=[(b'CMTR', b'Commuter'), (b'SHKN', b'Shinkansen'), (b'FRGT', b'Freight')])),
                ('series', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('length', models.IntegerField()),
                ('icon', models.ImageField(upload_to=b'')),
                ('photo', models.ImageField(upload_to=b'')),
                ('manufacturer', models.ForeignKey(to='trains.Manufacturer')),
            ],
        ),
    ]
