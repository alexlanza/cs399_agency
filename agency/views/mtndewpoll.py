from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from agency.models.mtndewpoll import MtnDewFlavorPoll
from django.contrib import messages
from django.http import Http404


class MtnDewPollForm(forms.Form):
    # class Meta:
    #     model = MtnDewFlavorPoll
    #     fields = ['flavor']

    flavor = forms.ChoiceField(
        choices=[('Cherry', 'Cherry'), ('Pineapple', 'Pineapple'), ('Berry', 'Berry'),
                 ('Mango', 'Mango')],
        widget=forms.Select(),
        label="Which flavor would you dew?")


def mtndewpoll(request):
    if request.method == 'POST':
        form = MtnDewPollForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thanks for voting!')
            flavor = form.cleaned_data['flavor']
            vote = MtnDewFlavorPoll(flavor=flavor)
            vote.save()
        else:
            messages.success(request, 'Something went wrong!')

        return render(request, "mtndewpoll.html", {'form': MtnDewPollForm()})

    elif request.method == 'GET':
        return render(request, "mtndewpoll.html", {'form': MtnDewPollForm()})
    else:
        raise Http404