from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == "GET":
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def product_detail(request, pk):
    try:
        product= Products.objects.get(pk = pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status = status.HTTP_200_OK)
    except: 
        product.DoesNotExist
        return Response(status.HTTP_404_NOT_FOUND)