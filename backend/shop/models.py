from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
# Create your models here.

class User(AbstractUser):
    phonenumber=models.CharField(max_length=11)
    is_admin=models.BooleanField(default=False)


class Order(models.Model):
    @property
    def purchase_amount(self):
        total_price=Product.objects.filter(order_products__order=self).aggregate(total=Sum('price'))['total']
        return total_price if total_price is not None else 0
    type=models.BooleanField(null=True,blank=True)



class Vertical(models.TextChoices):
    HOT_DRINK="hot drink"
    COLD_DRINK="cold drink"
    CAKE="cake"


class Product(models.Model):
    name=models.CharField(max_length=100)
    sugar=models.IntegerField()
    coffee=models.IntegerField()
    flour=models.IntegerField()
    vertical=models.CharField(max_length=100,choices=Vertical.choices,blank=False,null=False)
    price=models.IntegerField()

class OrderProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order_products")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_products")

class UserOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_orders")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="user_orders")
    is_active=models.BooleanField(default=True)


class Storage(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()

    
