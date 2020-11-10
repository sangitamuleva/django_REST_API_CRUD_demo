from django.db import models
from .product import Product
from .customer import Customer
import datetime
# Create your models here.
ORDER_CHOICES = ( 
    ("Processing", "Processing"), 
    ("Pending", "Pending"), 
    ("On Hold", "On Hold"), 
    ("Open", "Open"), 
    ( "Complete", "Complete"), 
    ("Closed", "Closed"), 
    ("Canceled", "Canceled"),
    
) 
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=500,default='a',blank=True,null=True)
    phone=models.CharField(max_length=50,default='a',blank=True,null=True)
    date=models.DateField(default= datetime.datetime.today)
    status = models.CharField( 
        max_length = 20, 
        choices = ORDER_CHOICES, 
        default='Processing'
        ) 
