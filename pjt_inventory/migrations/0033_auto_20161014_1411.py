# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-14 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0032_auto_20161014_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent_id',
            new_name='parent',
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pjt_inventory.Category'),
        ),
    ]