# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-26 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shower', '0015_auto_20160214_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='guess',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
