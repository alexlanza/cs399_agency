from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.forms import ModelForm

from agency.models.mp3 import Mp3Question, Mp3Choice, Mp3CollectedData


class Mp3Form(forms.Form):
    # list comprehension to get all of the choices for the first question, which has primary key=1
    SERVICE_CHOICES = [(c.choice_text, c.choice_text) for c in Mp3Question.objects.get(pk=1).mp3choice_set.all()]
    # all of the choices for question 2...
    GENRE_CHOICES = [(c.choice_text, c.choice_text) for c in Mp3Question.objects.get(pk=2).mp3choice_set.all()]
    # creates dropdown html "select" boxes using the above 2 variables as the options for the dropdowns
    service = forms.ChoiceField(choices=SERVICE_CHOICES,
                                widget=forms.Select(),
                                label="Please choose your favorite digital music service: ")
    genre = forms.ChoiceField(choices=GENRE_CHOICES,
                              label="Please choose your favorite genre of music: ")

    email = forms.EmailField(max_length=255, label="Please enter your email: ")

    # class Meta:
    #     model = Mp3Question
    #     fields = '__all__'


def mp3(request):
    success = ""
    collected_data = ""
    if request.method == 'POST':
        form = Mp3Form(request.POST)
        if form.is_valid():
            form.errors['success'] = "Success! Your mp3 is on the way."

            service = request.POST.get('service', '')
            genre = request.POST.get('genre', '')
            email = form.cleaned_data['email']
            mp3_collected_data = Mp3CollectedData(service=service, genre=genre, email=email)
            mp3_collected_data.save()
            return HttpResponseRedirect("/campaigns/mp3")
    elif request.method == 'GET':
        collected_data = Mp3CollectedData.objects.all()
        form = Mp3Form()
    else:
        return HttpResponseRedirect('/404/')
    return render(request, 'mp3.html', { 'form': form, 'collected_data': collected_data, 'success': success })