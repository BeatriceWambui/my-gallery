from django.shortcuts import render,redirect
from django.http import HttpResponse
# import datetime as dt
# Create your views here.

def welcome(request):
    return render (request,'index.html')

def personal_photos(request):
    return render (request,'all-photos/personal-photos.html')

def hobby_photos(request):
    return render (request,'all-photos/hobby-photos.html')