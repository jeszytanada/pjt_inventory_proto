# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-06 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0016_auto_20161006_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brands', to='pjt_inventory.Brand'),
        ),
    ]
