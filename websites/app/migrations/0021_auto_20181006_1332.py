# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20181006_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='cart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cus_cart_rel', to='app.Carts'),
        ),
    ]