# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20170714_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team_limit',
            field=models.IntegerField(default=2),
        ),
    ]