# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime

def initial_data(apps, schema_editor):
    data = {
        'What is your preferred music service?': ['Amazon', 'Google', 'iTunes', 'Spotify'],

        'What is your favorite genre of music?': ['Rap', 'Rock', 'Country', 'Electronic', 'Other']
    }
    Mp3Question = apps.get_model("agency", "Mp3Question")
    for question, choice in data.iteritems():
        q = Mp3Question(question_text=question, created=datetime.date.today())
        q.save()
        for item in choice:
            q.mp3choice_set.create(choice_text=item)

class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial')
    ]

    operations = [
        migrations.RunPython(initial_data)
    ]
