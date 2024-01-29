from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return render(request, "index.html")


def Resume(request):
    return render(request, "Resume.html")


def Signup(request):
    return render(request, "sign_up.html")


# Create your views here.
