# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20181003_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='owners',
            field=models.ManyToManyField(blank=True, null=True, to='app.Owners'),
        ),
    ]
