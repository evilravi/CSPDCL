# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-07-07 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0002_auto_20180705_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='Course',
        ),
        migrations.AddField(
            model_name='batch',
            name='Course',
            field=models.ManyToManyField(to='intern.Courses'),
        ),
    ]
