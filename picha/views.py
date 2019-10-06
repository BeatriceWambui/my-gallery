from django.shortcuts import render
from .models import Image,Location
# import datetime as dt
# Create your views here.

def welcome(request):
    return render (request,'index.html')

def personal_photos(request):
    return render (request,'all-photos/personal-photos.html')

def hobby_photos(request):
    return render (request,'all-photos/hobby-photos.html')

def search_results(request):
    if 'image'in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.searched_by_category(search_term)

        message = f'{search_term}'

        return render(request, 'all-photos/search.html',{'message':message,'images':searched_images})

    else:
        message = 'You havent searched for any image'
        return render(request,'all-images/search.html',{'message':message})