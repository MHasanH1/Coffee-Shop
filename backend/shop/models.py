from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    fullname=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=11)


class Order(models.Model):
    purchase_amount=models.IntegerField()
    type=models.BooleanField()


class Product(models.Model):
    pass
