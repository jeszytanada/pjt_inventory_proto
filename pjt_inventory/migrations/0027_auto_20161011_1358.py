# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-11 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0026_auto_20161011_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='child_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='parent_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
