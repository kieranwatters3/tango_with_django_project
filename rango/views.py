from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<a href='/rango/about/'>About</a> Rango says hey there partner!")


def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a> ")
