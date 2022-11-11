from rest_framework import serializers
from .models import Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'review_text', 'rating', 'name', 'product']
