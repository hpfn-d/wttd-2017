# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20170615_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
