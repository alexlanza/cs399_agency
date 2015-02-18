from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.db import models
	
def campaigns(request):
    return render(request, "campaigns.html", {})