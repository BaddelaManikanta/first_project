from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def snapchat(request):
    return HttpResponse('<h1><marquee>Hi Users Now We Are Using SnapChat</marquee></h1>')


def add(request):
    n1=int(input('Enter First Number : '))
    n2=int(input('Enter Second Number : '))
    res=n1+n2
    return HttpResponse(f'Result is = {res} !!!!!!!')