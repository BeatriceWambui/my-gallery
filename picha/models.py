from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     image_name = models.CharField(max_length = 40)
#     image_description = models.TextField()
#     user = models.ForeignKey(User)
#     category = models.ForeignKey(User)
#     location = models.ForeignKey(Location)

#     def __str__(self):
#         return self.name


