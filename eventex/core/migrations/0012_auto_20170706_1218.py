# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-06 12:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170630_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['start'], 'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
    ]
