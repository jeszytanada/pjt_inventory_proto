# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-06 06:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pjt_inventory', '0021_supplier_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('notes', models.TextField(null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_contacts', to='pjt_inventory.Supplier')),
            ],
        ),
    ]
