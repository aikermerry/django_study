# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=20)),
                ('wpwd', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'userinfos',
            },
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(verbose_name='书名', max_length=20),
        ),
    ]
