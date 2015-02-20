from django.shortcuts import render
from agency.models import Email
from django import forms
from django.http import Http404
from django.contrib import messages


class EmailForm(forms.Form):
    """
    Basic Django form for Email model.
    """
    class Meta:
        model = Email
        fields = ['email', 'first_name', 'last_name']

    email = forms.EmailField(label='Your email', required=True)
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)


def email(request):
    """
    Handles the email newsletter signup.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            x = Email()
            x.first_name = form.cleaned_data["first_name"]
            x.last_name = form.cleaned_data["last_name"]
            x.email = form.cleaned_data["email"]
            x.save()
            messages.success(request, 'Thanks for signing up! We promise not to spam you...')
        else:
            messages.success(request, 'Something went wrong...')
        return render(request, "email.html", {"form": EmailForm()})
    elif request.method == 'GET':
        return render(request, "email.html", {"form": EmailForm()})
    else:
        raise Http404()  # method not allowed
