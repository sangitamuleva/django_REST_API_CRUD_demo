from rest_framework import serializers
from .models.product import Product
from .models.order import Order
from .models.customer import Customer
from .models.category import Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields ='__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields ='__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields ='__all__'