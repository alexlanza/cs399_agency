from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.contrib import messages

from agency.models.mp3 import Mp3Question, Mp3Choice, Mp3CollectedData


class Mp3Form(forms.Form):
    # list comprehension to get all of the choices for the first question, which has primary key=1
    GENRE_CHOICES = [(c.choice_text, c.choice_text) for c in Mp3Question.objects.get(pk=1).mp3choice_set.all()]
    # all of the choices for question 2...
    SERVICE_CHOICES = [(c.choice_text, c.choice_text) for c in Mp3Question.objects.get(pk=2).mp3choice_set.all()]
    # creates dropdown html "select" boxes using the above 2 variables as the options for the dropdowns
    service = forms.ChoiceField(choices=SERVICE_CHOICES,
                                widget=forms.Select(),
                                label="Please choose your favorite digital music service ")
    genre = forms.ChoiceField(choices=GENRE_CHOICES,
                              label="Please choose your favorite genre of music ")

    email = forms.EmailField(max_length=255, label="Please enter your email ")


def _get_service_votes():
    services = {"Amazon": 0, "Google": 0, "iTunes": 0, "Spotify": 0}
    for service in services:
        votes = Mp3CollectedData.objects.filter(service=service).count()
        services[service] = votes
    return services


def _get_genre_votes():
    genres = {"Rap": 0, "Rock": 0, "Country": 0, "Electronic": 0, "Other": 0}
    for genre in genres:
        votes = Mp3CollectedData.objects.filter(genre=genre).count()
        genres[genre] = votes
    return genres


def mp3(request):
    if request.method == 'POST':

        form = Mp3Form(request.POST)
        if form.is_valid():
            messages.success(request, 'Success! Check your email for your free mp3 download')
            service = request.POST.get('service', '')
            genre = request.POST.get('genre', '')
            email = form.cleaned_data['email']
            # save the new information in the Mp3CollectedData table
            mp3_collected_data = Mp3CollectedData(service=service, genre=genre, email=email)
            mp3_collected_data.save()
            return HttpResponseRedirect("/campaigns/mp3")
    elif request.method == 'GET':
        form = Mp3Form()
    else:
        return HttpResponseRedirect('/')
    # get all the data people have entered thus far in the Mp3CollectedData table
    service_votes = _get_service_votes()
    genre_votes = _get_genre_votes()
    return render(request, 'mp3.html', { 'form': form, 'service_votes': service_votes, 'genre_votes': genre_votes })