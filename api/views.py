from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics,permissions
from rest_framework.response import Response
from .models.product import Product
from .models.order import Order
from .models.customer import Customer
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as K_LoginView
from .models.category import Category
from django.contrib.auth import login
from .serializer import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import IntegrityError
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
    serializer=CategorySerializer(category,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def category_update(request,pk):
    # print(request.data)
    category=Category.objects.get(id=pk)
    serializer=CategorySerializer(instance=category,data=request.data,many=False)

    if serializer.is_valid():
        serializer.save()
    print(serializer)
    return Response(serializer.data)
# Create your views here.

@api_view(['DELETE'])
def category_delete(request,pk):
    print(pk)
    category=Category.objects.get(id=pk)
    category.delete()
    return Response("Product Deleted")




# Register API
class Register_user(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        # print(request.data)
            serializer = self.get_serializer(data=request.data)
       
        # try:
            serializer.is_valid(raise_exception=True)
        

            user = serializer.save()
        
            user.set_password(user.password)
            user.save()
            return Response({
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
                "message":"User created Successfully!!"
            })

        # except  IntegrityError as err:
        #     print(err)
        #     # raise serializers.ValidationError("finish must occur after start")
        #     return Response({'username':err.args[1]})
        
# Login API
class Login_user(K_LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        print(user)
        login(request, user)
        return super(Login_user, self).post(request, format=None)

from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.core.mail import send_mail  

# @receiver(reset_password_token_created)
# def password_reset_token(sender,instance,reset_password_token,*args, **kwargs):
#     email_plaintext_message ="{}?token={}".format(
#             instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
#             reset_password_token.key)
#     send_mail(
#         # title:
#         "Password Reset for {title}".format(title="EFashion.com"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email]
#     )

#     return Response({"message":"Email Sent !!"})

@receiver(reset_password_token_created)
def password_reset_token(sender,instance,reset_password_token,*args, **kwargs):

    email_plaintext_message ="click here: http://localhost:3000/reset_password \n token={}".format(
                       reset_password_token.key)

    # print(*args)
    print(instance.request.data)

    if instance.request.data.get('username'):
        user=User.objects.get(username=instance.request.data.get('username'))
        # print(user.email)

        if reset_password_token.user.email == user.email:
            send_mail(
                # title:
                "Password Reset for {title}".format(title="EFashion.com"),
                # message:
                email_plaintext_message,
                # from:
                "noreply@somehost.local",
                # to:
                [reset_password_token.user.email]
            )

    return Response({"message":"Email Sent !!"})

