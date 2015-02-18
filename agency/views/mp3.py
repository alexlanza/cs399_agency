from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.forms import ModelForm

from agency.models.mp3 import Mp3Question, Mp3Choice


class Mp3Form(forms.ModelForm):
    class Meta:
        model = Mp3Question
        fields = ['question_text','email']


def mp3(request):
    if request.method == 'POST':
        form = Mp3Form(request.POST)
        if form.is_valid():
            mp3 = Mp3Question()
            mp3.question_text = form.cleaned_data['question_text']
            mp3.email = form.cleaned_data['email']
            return HttpResponseRedirect("/mp3/")
    elif request.method == 'GET':
        form = Mp3Form()
    else:
        return HttpResponseRedirect('/404/')
    return render(request, 'mp3.html', { 'form': form })