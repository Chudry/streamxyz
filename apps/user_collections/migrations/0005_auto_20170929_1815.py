# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_collections', '0004_collectionitemmodel_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionitemmodel',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
