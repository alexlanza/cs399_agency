from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from agency.models import email_model

class emailForm(forms.Form):
	class Meta:
		model = email_model
		fields = ['email', 'firstname', 'lastname']
		
	email = forms.EmailField(label='Your email', required=True)
	firstname = forms.CharField(max_length=128, required=True)
	lastname = forms.CharField(max_length=128,required=True)
	

