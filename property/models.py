from decimal import Clamped
from distutils.command.upload import upload
from turtle import up
from unicodedata import category, name
from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=10000)
    place = models.ForeignKey('Place', related_name='property_place',on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='property_category',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages/')
    
    def __str__(self):
        return str(self.property)


class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='palce/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
