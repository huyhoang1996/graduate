# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20190425_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Products'),
        ),
    ]
