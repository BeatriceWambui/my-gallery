from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.personal_photos,name ='myPhotos'),
    url(r'^$',views.hobby_photos,name='hobbyPhotos'),
]