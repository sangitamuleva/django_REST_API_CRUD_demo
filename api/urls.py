from django.urls import path
from .views import *
from knox import views as knox_views

urlpatterns = [
    # path('',product_list,name="product_list"),    
    # path('create/',product_create,name="product_create"),
    # path('<pk>/',product_detail,name="product_detail"),
    # path('update/<pk>/',product_update,name="product_update"),
    # path('delete/<pk>/',product_delete,name="product_delete"),

    path('category/',category_list,name="category_list"),    
    path('category/create/',category_create,name="category_create"),
    path('category/<pk>/',category_detail,name="category_detail"),
    path('category/update/<pk>/',category_update,name="category_update"),
    path('category/delete/<pk>/',category_delete,name="category_delete"),
    path('user/register/', Register_user.as_view(), name='register'),
    path('user/login/', Login_user.as_view(), name='login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]