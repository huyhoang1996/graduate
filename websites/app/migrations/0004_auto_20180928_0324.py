# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-28 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180928_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipinfomations',
            name='address',
            field=models.EmailField(max_length=250, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='shipinfomations',
            name='email',
            field=models.EmailField(blank=True, max_length=250, verbose_name='email'),
        ),
    ]