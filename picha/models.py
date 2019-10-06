from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 40)
    image_description = models.TextField()
    editor = models.CharField(max_length=50,default='admin')
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images

    def __str__(self):
        return self.image_name




