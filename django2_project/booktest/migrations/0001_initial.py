# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField()),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(verbose_name='姓名', max_length=20)),
                ('hgender', models.BooleanField(verbose_name='性别', default=True)),
                ('isdelete', models.BooleanField(default=0)),
                ('hconment', models.CharField(verbose_name='简介', max_length=100)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
            options={
                'db_table': 'heroinfo',
            },
        ),
    ]
