# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0006_auto_20150219_1803'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='email_model',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
