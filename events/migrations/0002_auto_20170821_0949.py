# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='plug_ins',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
