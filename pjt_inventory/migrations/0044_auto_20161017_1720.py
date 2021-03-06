# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-17 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0043_auto_20161017_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_stock', to='pjt_inventory.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductStockHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('reference_type', models.IntegerField(default=0)),
                ('reference_id', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_stock_history', to='pjt_inventory.Product')),
            ],
        ),
        migrations.RenameField(
            model_name='productattribute',
            old_name='product_id',
            new_name='product',
        ),
    ]
