# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-26 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_review', '0036_auto_20180203_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='questionLabel',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='label',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
