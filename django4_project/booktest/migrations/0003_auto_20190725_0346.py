# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190725_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='wpwd',
            new_name='upwd',
        ),
    ]
