# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_stores_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='detail',
            field=models.TextField(blank=True, verbose_name='detail'),
        ),
    ]