from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Products


# Create your models here.

class Review(models.Model):
    review_text = models.CharField(max_length = 255)
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)


