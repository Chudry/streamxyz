# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_streams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamitemmodel',
            name='blacklist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='streammodel',
            name='blacklist',
            field=models.BooleanField(default=False),
        ),
    ]
