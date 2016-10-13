# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-05 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pjt_inventory', '0006_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='brand',
            old_name='created_date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='updated_date',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='brand_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created_date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='published_date',
            new_name='date_publish',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='updated_date',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='desc_en',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='desc_header',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='created_date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='updated_date',
            new_name='date_updated',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_contact',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='brand',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='retail_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='product',
            name='wholesale_price',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_contact_person',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='supplier_name',
        ),
        migrations.AddField(
            model_name='brand',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='brand',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brand_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pjt_inventory.Brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='free_shipping',
            field=models.CharField(choices=[('Always', 'Always'), ('Normal', 'Normal'), ('Special', 'Special')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='order_max',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='order_min',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='price_bought',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='price_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='price_retail',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='price_wholesale',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='remarks',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size_flag',
            field=models.CharField(choices=[('RE', 'Regular'), ('SA', 'Sample'), ('TE', 'Tester'), ('OT', 'Others')], default='RE', max_length=2),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pjt_inventory.Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='fax',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='phone',
            field=models.CharField(default='000-0000', max_length=50),
        ),
        migrations.AddField(
            model_name='supplier',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='tags',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='tax_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='supplier',
            name='zipcode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]