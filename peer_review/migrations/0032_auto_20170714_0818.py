# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-14 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peer_review', '0031_auto_20170714_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userId',
            new_name='user_id',
        ),
    ]
