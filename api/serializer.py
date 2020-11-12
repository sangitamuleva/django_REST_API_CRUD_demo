from rest_framework import serializers,permissions
from .models.product import Product
from .models.order import Order
from .models.customer import Customer
from .models.category import Category
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# from django.contrib.auth.hashers import set_password

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id','username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        # def create(self, validated_data):
        #     user = User(username=validated_data['username'],email= validated_data['email'])
        #     user.make_password(validated_data['password'])
        #     user.save()
        #     return user

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            # instance.save()
            return instance