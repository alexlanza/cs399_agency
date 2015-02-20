# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_auto_20150219_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_model',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='email_model',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
