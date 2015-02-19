from django.db import models
from django.forms import ModelForm

class MtnDewFlavorPoll(models.Model):
    flavor = models.CharField(max_length=200)
    votes = models.IntegerField()
    def __unicode__(self):
        return self.flavor

