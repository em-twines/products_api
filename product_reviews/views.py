from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Review
from .serializer import ReviewSerializer
# from products.serializers import ProductSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == "GET":
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)




@api_view(["GET", "PUT", "DELETE"])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk = pk)
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = ReviewSerializer(review, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



@api_view(["GET", "PUT", "DELETE"])
def review_by_product(request, product_id):
    reviews = Review.objects.filter(product_id = product_id)
    if request.method == "GET":
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
