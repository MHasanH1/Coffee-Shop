from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phonenumber=models.CharField(max_length=11)
    is_admin=models.BooleanField(default=False)


class Order(models.Model):
    purchase_amount=models.IntegerField()
    type=models.BooleanField()



class Vertical(models.TextChoices):
     HOT_DRINK="hot drink"
     COLD_DRINK="cold drink"
     CAKE="cake"


class Product(models.Model):
    name=models.CharField(max_length=100)
    sugar=models.IntegerField()
    coffee=models.IntegerField()
    flour=models.IntegerField()
    vertical=models.CharField(max_length=100,choices=Vertical.choices)
    price=models.IntegerField()

class OrderProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order_products")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_products")

class UserOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_orders")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="user_orders")


class Storage(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()

    
