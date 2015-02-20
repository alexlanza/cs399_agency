# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_auto_20150220_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mtndewflavorpoll',
            name='votes',
        ),
    ]
