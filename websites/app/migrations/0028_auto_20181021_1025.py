# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_orderinfomations_payer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdetail',
            name='quanlity',
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='quanlity',
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=3, verbose_name='quantity'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(default=3, verbose_name='quantity'),
            preserve_default=False,
        ),
    ]
