from django.shortcuts import render
from .models import Image,Location
# import datetime as dt
# Create your views here.

def index(request):
    images = Image.objects.all()
    location = Location.objects.all()
   
    return render (request,'all-photos/index.html',{'images':images, 'location':location})

def personal_photos(request):
    return render (request,'all-photos/personal-photos.html')

def hobby_photos(request):
    return render (request,'all-photos/hobby-photos.html')



def search_results(request):
    if 'image'in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images = Image.search_by_category(search_term)

        message = f'{search_term}'
        print(searched_images)
        return render(request, 'all-photos/search.html',{'message':message,'images':searched_images})

    else:
        message = 'You havent searched for any image'
        return render(request,'all-images/search.html',{'message':message})

def search_location(request,id):
    location = Location.objects.all()
    photo = Image.objects.filter(location__id = id)

    return render(request, 'all-photos/location.html',{'location':location,'photo':photo})
