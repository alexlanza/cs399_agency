# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_auto_20150219_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='MtnDewFlavorPoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flavor', models.CharField(max_length=200)),
                ('votes', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
