# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 05:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0011_auto_20180326_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='assets.Domain', verbose_name='Domain'),
        ),
    ]
