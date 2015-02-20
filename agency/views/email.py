from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from agency.models import Email
from django import forms
from django.http import HttpResponseRedirect
from django.db import models


class EmailForm(forms.Form):
    class Meta:
        model = Email
        fields = ['email', 'first_name', 'last_name']

    email = forms.EmailField(label='Your email', required=True)
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            x = Email()
            x.first_name = form.cleaned_data["first_name"]
            x.last_name = form.cleaned_data["last_name"]
            x.email = form.cleaned_data["email"]
            x.save()
            return HttpResponseRedirect('/campaigns')
    elif request.method == 'GET':
        form = EmailForm()
    else:
        return HttpResponseRedirect("/campaigns")
    return render(request, "email.html", {"form": form})
