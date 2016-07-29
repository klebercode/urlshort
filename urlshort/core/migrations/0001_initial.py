# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-28 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('slug_key', models.SlugField(max_length=6, primary_key=True, serialize=False, verbose_name='Chave')),
                ('my_url', models.URLField(verbose_name='Link')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
                ('count', models.IntegerField(default=0, verbose_name='Cliques')),
            ],
        ),
    ]