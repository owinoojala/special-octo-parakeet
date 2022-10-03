from distutils.command.upload import upload
from django.db import models

# Create your models here.
class PaymentMethods(models.Model):
    img = models.ImageField(upload_to='pics', null=True)
class Address(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    desc = models.TextField()
    physical_address = models.CharField(max_length=200)

class Vendor(models.Model):
    img = models.ImageField(upload_to='pics', null=True)

class Latest(models.Model):
    img = models.ImageField(upload_to='pics', null=True)
    name = models.CharField(max_length=200)
    previous_price = models.FloatField()
    current_price = models.FloatField()
class SpecialCollection(models.Model):
    img = models.ImageField(upload_to='pics', null=True)
    name = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    offer = models.BooleanField(default=False)

class Carousel(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics', null=True)
    discount = models.CharField(max_length=200)
class Product(models.Model):
    men_dress = models.BooleanField()
    women_dress = models.BooleanField()
    babies_dress = models.BooleanField()
    jeans = models.BooleanField()
    shirt = models.BooleanField()
    swimwear = models.BooleanField()
    sleepwear = models.BooleanField()
    sportswear = models.BooleanField()
    jumpsuit = models.BooleanField()
    blazer = models.BooleanField()
    jacket = models.BooleanField()
    shoe = models.BooleanField()
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics', null=True)
    current_price = models.FloatField()
    previous_price = models.FloatField()

class Category(models.Model):
    name = models.CharField(max_length=200)
    stock_count = models.IntegerField()
    img = models.ImageField(upload_to='pics', null=True)

class Order(models.Model):
    front_view_image = models.ImageField(upload_to = 'pics', null=True)
    rare_view_image = models.ImageField(upload_to = 'pics', null=True)
    side_view_image = models.ImageField(upload_to = 'pics', null=True)
    


