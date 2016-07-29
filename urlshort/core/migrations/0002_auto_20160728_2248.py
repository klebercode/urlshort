# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-29 01:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='created_at',
        ),
        migrations.AddField(
            model_name='link',
            name='last_access',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 29, 1, 48, 44, 145940, tzinfo=utc), verbose_name='Último Acesso'),
            preserve_default=False,
        ),
    ]
