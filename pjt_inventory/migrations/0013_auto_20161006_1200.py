# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-06 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0012_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='brands', to='pjt_inventory.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='suppliers', to='pjt_inventory.Supplier'),
        ),
    ]
