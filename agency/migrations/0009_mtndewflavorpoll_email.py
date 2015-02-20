# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_remove_mtndewflavorpoll_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtndewflavorpoll',
            name='email',
            field=models.EmailField(max_length=254, null=True),
            preserve_default=True,
        ),
    ]
