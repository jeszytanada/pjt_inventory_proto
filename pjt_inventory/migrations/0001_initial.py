# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-09-29 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('size', models.IntegerField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(max_length=1000)),
                ('manufacturer', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('barcode', models.BigIntegerField()),
                ('retail_price', models.BigIntegerField()),
                ('wholesale_price', models.BigIntegerField()),
                ('weight', models.IntegerField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
