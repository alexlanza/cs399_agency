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
        choices=[('Mtn Dew', 'Mtn Dew'), ('Diet Mtn Dew', 'Diet Mtn Dew'), ('Mountain Dew Code Red', 'Mountain Dew Code Red'),
                 ('Mountain Dew Live Wire', 'Mountain Dew Live Wire'),
                 ('Mountain Dew Voltage', 'Mountain Dew Voltage'),
                 ('Mountain Dew White Out', 'Mountain Dew White Out'),
                 ('Mountain Dew Throw Back', 'Mountain Dew Throw Back')],
        widget=forms.Select(),
        label="Which flavor do you dew?")
    email = forms.EmailField(max_length=255, label="Please enter your email ")
		
def mtndewpoll(request):
    if request.method == 'POST':
        form = MtnDewPollForm(request.POST)
        if form.is_valid():
			messages.success(request, 'Thanks for voting!')
			flavor = form.cleaned_data['flavor']
			email = form.cleaned_data['email']
			vote = MtnDewFlavorPoll(flavor=flavor, email=email)
			vote.save()
        else:
            messages.success(request, 'Something went wrong!')

        return render(request, "mtndewpoll.html", {'form': MtnDewPollForm()})

    elif request.method == 'GET':
        return render(request, "mtndewpoll.html", {'form': MtnDewPollForm()})
    else:
        raise Http404