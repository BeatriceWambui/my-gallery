from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

class category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name