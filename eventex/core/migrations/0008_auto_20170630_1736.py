# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 17:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('core', '0007_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
    ]
