# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-13 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regist_index', '0002_auto_20190813_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='recvusername',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
