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
    sugar=models.PositiveIntegerField()
    coffee=models.PositiveIntegerField()
    flour=models.PositiveIntegerField()
    vertical=models.CharField(max_length=100,choices=Vertical.choices,blank=False,null=False)
    price=models.PositiveIntegerField()

class OrderProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order_products")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_products")

    def check_product(self):
        storage_sugar=Storage.objects.get(name="sugar").amount
        storage_coffee=Storage.objects.get(name="coffee").amount
        storage_flour=Storage.objects.get(name="flour").amount
        storage_chocolate=Storage.objects.get(name="chocolate").amount
        if self.product.sugar > storage_sugar:
            return False,"sugar"
        if self.product.coffee > storage_coffee:
            return False,"coffee"
        if self.product.flour > storage_flour:
            return False,"flour"
        # if self.product.sugar < storage_sugar:
        #     return False,(self.product.sugar,storage_sugar)
        return True,()
         

class UserOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_orders")
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="user_orders")
    is_active=models.BooleanField(default=True)
    datetime=models.DateTimeField(blank=True,null=True)


class Supply(models.TextChoices):
    SUGAR="sugar"
    COFFEE="coffee"
    FLOUR="flour"
    CHOCOLATE="chocolate"

class Storage(models.Model):
    name=models.CharField(max_length=100,choices=Supply.choices)
    amount=models.PositiveIntegerField(default=0)

    
