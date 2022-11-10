from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=7, decimal_places = 2)
    inventory_quantity = models.IntegerField(default = 0)
    image_link = models.CharField(max_length=255, default = 'https://assets-eu-01.kc-usercontent.com/559bb7d3-88a4-01c1-79a3-dd4d5b2d2bb0/b952b71e-20ff-4434-9486-5aa0b4378145/1-French-Baguettes.jpg?w=1920&q=85&auto=format&lossless=1')
