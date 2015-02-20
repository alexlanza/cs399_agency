# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_mp3collecteddata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='email',
            new_name='email_model',
        ),
    ]
