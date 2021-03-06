# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-05 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayWeek', models.CharField(max_length=264, unique=True)),
                ('discipline', models.CharField(max_length=264, unique=True)),
                ('group', models.CharField(max_length=264, unique=True)),
                ('teacher', models.CharField(max_length=264, unique=True)),
                ('classroom', models.CharField(max_length=264, unique=True)),
                ('isLecture', models.BooleanField()),
            ],
        ),
    ]
