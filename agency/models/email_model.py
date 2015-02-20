from django.db import models

class email_model(models.Model):
	firstname = models.CharField(default="", max_length=128)
	lastname = models.CharField(default="", max_length=128)
	email = models.EmailField()