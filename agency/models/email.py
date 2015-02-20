from django.db import models


class Email(models.Model):
    first_name = models.CharField(default="", max_length=128)
    last_name = models.CharField(default="", max_length=128)
    email = models.EmailField()