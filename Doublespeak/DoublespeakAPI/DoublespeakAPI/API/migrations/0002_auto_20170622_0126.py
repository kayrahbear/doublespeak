# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='election_year',
            field=models.CharField(max_length=4),
        ),
    ]
