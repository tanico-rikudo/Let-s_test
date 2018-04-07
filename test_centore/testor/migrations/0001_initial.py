# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-07 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.CharField(max_length=255, verbose_name='E-Mail')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='Age')),
            ],
        ),
    ]
