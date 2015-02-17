from djago.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.models import email
from django import froms
from django.http import HttpResponseRedirect
from django.db import models
from agency.forms import emailForm

def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})
	
def thanks(request):
	return render(request, 'thanks.html', {})
	
def campaigns(request):
	return render(request, 'campaigns.html', {})
	
def mp3(request):
	return render(request, 'mp3.html', {})
	
def poll(request):
	return render(request, 'poll.html', {})
	
def email(request):
	return render(request, 'email.html', {})
	
def email(request):
    if request.method == 'POST':
	    form = Contest1Form(request.POST)
	    if form.is_valid():
		    x = email()
		    x.firstname = form.cleaned_data["firstname"]
			x.lastname = form.cleaned_data["lastname"]
			x.email = form.cleaned_data["email"]
		    x.save()
		    return HttpResponseRedirect("/thanks")
    elif request.method == 'GET':
	    form = Contest1Form()
    else:
	    return HttpResponseRedirect("/404/")
		
    return render(request, "email.html", {"form" : form})