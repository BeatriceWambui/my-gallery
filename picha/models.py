from django.db import models

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length =40)
#     last_name = models.CharField(max_length =40)
#     email = models.EmailField()

#     def __str__(self):
#         return self.first_name
#     class Meta:
#         ordering = ['first_name']

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length = 40)
    image_description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    @classmethod
    def search_by_category(cls,category):
        photo=cls.objects.filter(category__name__icontains=category)
        return photo

    def __str__(self):
        return self.name


