# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-14 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0033_auto_20161014_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_id',
            new_name='category',
        ),
    ]
