# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-12 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfs', '0002_auto_20170512_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='countryId',
        ),
    ]
