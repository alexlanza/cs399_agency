from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from agency.models import email


class emailForm(forms.Form):
	class Meta:
		model = email
		fields = ['email', 'firstname', 'lastname']	
	email = new forms.Email.Field(label='Your email, required=True)
	firstname = forms.CharField(max_length=128)
	lastname = forms.CharField(max_length=128)
	

