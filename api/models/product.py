from django.db import models
from .category import Category
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='uploads/products/')

    # @staticmethod
    # def get_product_by_category(id):
    #     if id:
    #         return Product.objects.filter(category=id)
    #     else :
    #         return Product.objects.all()