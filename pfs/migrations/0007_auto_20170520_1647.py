# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-20 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfs', '0006_auto_20170520_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True),
        ),
    ]