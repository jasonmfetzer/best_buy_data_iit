# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-30 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20171130_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]