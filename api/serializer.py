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
       
        # def validate_username(self, value):
        #     check_query = User.objects.filter(username=value)
        #     if self.instance:
        #         check_query = check_query.exclude(pk=self.instance.pk)

        #     if self.parent is not None and self.parent.instance is not None:
        #         user = getattr(self.parent.instance, self.username)
        #         check_query = check_query.exclude(pk=user.pk)

        #     if check_query.exists():
        #         raise serializers.ValidationError('Username already exists.')

        #     print(value)
        #     print('----')
        #     return value
        # def create(self, validated_data):
        #     print("----------- creater")
        #     user = User(username=validated_data['username'],email= validated_data['email'])
        #     user.password=make_password(validated_data['password'])
        #     # user.save()
        #     return user

        # def create(self, validated_data):
        #     print("----------- creater")
        #     password = validated_data.pop('password', None)
        #     instance = self.Meta.model(**validated_data)
        #     if password is not None:
        #         instance.set_password(password)
        #     # instance.save()
        #     return instance