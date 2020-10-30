from django.urls import path
from .views import *

urlpatterns = [
    path('',product_list,name="product_list"),    
    path('create/',product_create,name="product_create"),
    path('<pk>/',product_detail,name="product_detail"),
    path('update/<pk>/',product_update,name="product_update"),
    path('delete/<pk>/',product_delete,name="product_delete"),

]