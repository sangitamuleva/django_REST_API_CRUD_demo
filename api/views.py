from django.shortcuts import render
from rest_framework.decorators import api_view

from .models.product import Product
from .models.order import Order
from .models.customer import Customer
from .models.category import Category

from .serializer import *

from rest_framework.response import Response

# @api_view(['POST'])
# def product_create(request):
#     serializer=ProductSerializer(data=request.data,many=False)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['GET'])
# def product_list(request):
#     products=Product.objects.all()
#     serializer=ProductSerializer(products,many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def product_detail(request,pk):
#     product=Product.objects.get(id=pk)
#     serializer=ProductSerializer(product,many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def product_update(request,pk):
#     product=Product.objects.get(id=pk)
#     serializer=ProductSerializer(instance=product,data=request.data,many=False)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
# # Create your views here.

# @api_view(['DELETE'])
# def product_delete(request,pk):
#     product=Product.objects.get(id=pk)
#     product.delete()
#     return Response("Product Deleted")


@api_view(['POST'])
def category_create(request):
    print(request.data.get("category_name"))
    serializer=CategorySerializer(data=request.data,many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request,pk):
    category=Category.objects.get(id=pk)
    serializer=CategorySerializer(product,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def category_update(request,pk):
    print(request.data)
    category=Category.objects.get(id=pk)
    serializer=CategorySerializer(instance=category,data=request.data,many=False)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# Create your views here.

@api_view(['DELETE'])
def category_delete(request,pk):
    category=Category.objects.get(id=pk)
    category.delete()
    return Response("Product Deleted")
