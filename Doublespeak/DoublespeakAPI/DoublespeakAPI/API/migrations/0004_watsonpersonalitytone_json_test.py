# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-22 10:35
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_candidate_short_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='watsonpersonalitytone',
            name='json_test',
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]
