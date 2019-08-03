# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areasInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('pid', models.ForeignKey(to='booktest.areasInfo')),
            ],
            options={
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('btitle', models.CharField(max_length=20)),
                ('bpub_date', models.DateTimeField()),
                ('bread', models.IntegerField()),
                ('bcomment', models.IntegerField()),
                ('isDelete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hname', models.CharField(max_length=20)),
                ('hgender', models.BooleanField(default=0)),
                ('isdelete', models.BooleanField(default=0)),
                ('hcontent', models.CharField(max_length=100)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
            options={
                'db_table': 'heroinfo',
            },
        ),
        migrations.CreateModel(
            name='text',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('hcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'userinfos',
            },
        ),
    ]
