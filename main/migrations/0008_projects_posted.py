# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180220_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='posted',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
    ]
