from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html", {})
	
def email(request):
    return render(request, "email.html", {})

def email(request):
    return render(request, "about.html", {})