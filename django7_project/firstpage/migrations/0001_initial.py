# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-04 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('phonenum', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('is_delete', models.BooleanField(default=0)),
                ('upub_date', models.DateField()),
            ],
            options={
                'db_table': 'userinfo',
            },
            managers=[
                ('manage', django.db.models.manager.Manager()),
            ],
        ),
    ]
