from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from django import forms
from agency.models.mtndewpoll import MtnDewFlavorPoll

class MtnDewPollForm(forms.ModelForm):
    class Meta:
        model = MtnDewFlavorPoll
        fields = ['flavor']
	
def mtndewpoll(request):
    return render(request, "mtndewpoll.html", {'form': MtnDewPollForm})
