# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-08 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_auto_20181122_0429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfomations',
            name='money',
            field=models.IntegerField(blank=True, null=True, verbose_name='money'),
        ),
    ]
