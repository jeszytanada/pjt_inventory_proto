# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-14 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0038_auto_20161014_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='category',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tags',
        ),
        migrations.AddField(
            model_name='category',
            name='is_child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pjt_inventory.Category'),
        ),
    ]
