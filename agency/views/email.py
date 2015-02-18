from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from agency.models import email
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
from agency.forms import emailForm
	
def email(request):
    return render(request, "email.html", {})
#def email(request):
#	if request.method == 'POST':
#		emailForm = Contest1Form(request.POST)
#	if form.is_valid():
#		x = email()
#		x.firstname = form.cleaned_data["firstname"]
#		x.lastname = form.cleaned_data["lastname"]
#		x.email = form.cleaned_data["email"]
#		x.save()
#		return HttpResponseRedirect("/thanks")
#	elif request.method == 'GET':
# 	    form = Contest1Form()
#	else:
#		return render(request, "email.html", {"form" : form})
