# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peer_review', '0023_auto_20160312_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text=b'Designates whether this user should be treated as active. Deselect this instead of deleting accounts.'),
        ),
    ]
