# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=50)),
                ('most_used_words', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive_sentiment', models.IntegerField()),
                ('negative_sentiment', models.IntegerField()),
                ('sentiment_confidence', models.DecimalField(decimal_places=2, max_digits=4)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='WatsonEmotionalTone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anger_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('disgust_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fear_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('joy_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sadness_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='WatsonPersonalityTone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openness_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('conscientiousness_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('extraversion_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('agreeableness_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('emotional_range_tone', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='election_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Election'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Party'),
        ),
    ]
