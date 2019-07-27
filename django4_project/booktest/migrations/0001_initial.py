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
                ('btitle', models.CharField(verbose_name='目录', max_length=20)),
                ('bpub_date', models.DateTimeField(verbose_name='时间')),
                ('bread', models.IntegerField(verbose_name='阅读量', default=0)),
                ('bcomment', models.IntegerField(verbose_name='评论量', default=0)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=0)),
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
                ('hgender', models.BooleanField(verbose_name='性别', default=0)),
                ('isDelete', models.BooleanField(verbose_name='是否删除', default=0)),
                ('hcontent', models.CharField(verbose_name='简介', max_length=100)),
                ('hbook', models.ForeignKey(to='booktest.BookInfo')),
            ],
            options={
                'db_table': 'heroinfo',
            },
        ),
    ]
