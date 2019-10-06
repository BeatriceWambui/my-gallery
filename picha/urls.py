from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.personal_photos,name ='myPhotos'),
    url(r'^$',views.hobby_photos,name='hobbyPhotos'),
    url(r'^search/',views.search-results,name='search_results')
]

if settings.Debug:
    urlpatterns+= static(settings.MEDIA_url,document_root = settings.MEDIA_ROOT)