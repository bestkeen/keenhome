# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-29 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180429_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team_belong',
            field=models.CharField(default='C640', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='job_join_time',
            field=models.CharField(default='2011-10-10', max_length=20),
        ),
    ]