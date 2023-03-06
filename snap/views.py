from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def snapchat(request):
    return HttpResponse('<h1><marquee>Hi Users Now We Are Using SnapChat</marquee></h1>')
