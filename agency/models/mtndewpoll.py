from django.db import models

class MtnDewFlavorPoll(models.Model):
	flavor = models.CharField(max_length=200)
	email = models.EmailField(max_length=254, null=True)
	def __unicode__(self):
		return self.flavor