# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_mtndewflavorpoll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mp3CollectedData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now=True, verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
