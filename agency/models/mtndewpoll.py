from django.db import models

class MtnDewFlavorPoll(models.Model):
    flavor = models.CharField(max_length=200)

    def __unicode__(self):
        return self.flavor

