from django.db import models


class Mp3Question(models.Model):
    question_text = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    created = models.DateTimeField('date created')


class Mp3Choice(models.Model):
    question = models.ForeignKey(Mp3Question)
    choice_text = models.CharField(max_length=255)

