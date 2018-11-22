# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-18 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_products_price_usd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderinfomations',
            name='money_usd',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price_usd',
        ),
        migrations.RemoveField(
            model_name='products',
            name='status',
        ),
        migrations.AddField(
            model_name='products',
            name='count_in_stock',
            field=models.IntegerField(default=40, verbose_name='count in stock'),
            preserve_default=False,
        ),
    ]