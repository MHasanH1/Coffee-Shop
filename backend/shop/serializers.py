from rest_framework import serializers
from .models import User,Product,OrderProduct,UserOrder,Order,Storage
from django.utils import timezone
from collections import defaultdict
from datetime import datetime, timedelta

class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User

        fields=('username','password','email','phonenumber','first_name','last_name','is_admin')


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phonenumber=validated_data['phonenumber']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    in_cart = serializers.SerializerMethodField()
    count_in_cart=serializers.SerializerMethodField()
    class Meta:
        model=Product
        fields=('id','name','sugar','coffee','flour','vertical','price','in_cart','count_in_cart')
    
    def create(self,validated_data):
        product=Product(
            name=validated_data['name'],
            sugar=validated_data['sugar'],
            coffee=validated_data['coffee'],
            flour=validated_data['flour'],
            vertical=validated_data['vertical'],
            price=validated_data['price']
        )
        product.save()
        return product
    
    def get_in_cart(self,obj:Product):
        user=self.context['request'].user
        user_orders=UserOrder.objects.filter(user=user,order__order_products__product=obj)
        if user_orders.exists():
            return user_orders.last().is_active
        return False
    
    def get_count_in_cart(self,obj:Product):
        user=self.context['request'].user
        cart=UserOrder.objects.filter(user=user,is_active=True).last()
        if cart!=None:
            order_products=OrderProduct.objects.filter(order=cart.order,product=obj) 
            return order_products.count()
        else:
            return 0

        
    

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields=('id','product','order')



    

    

class OrderSerializer(serializers.ModelSerializer):
    products=serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields=('id','products','purchase_amount','type')
    
    def get_products(self,obj:Order):
        products=Product.objects.filter(order_products__order=obj)
        return ProductSerializer(products,many=True,context=self.context).data
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=('id','first_name','last_name','email','phonenumber','username','is_admin')


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model =Storage
        fields = ('name','amount')


class UserOrderSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    order=OrderSerializer()
    class Meta:
        model = UserOrder
        fields= ('id','user','order','is_active','datetime')



class CustomProductSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id','name', 'history']

    def get_history(self, obj):
        three_months_ago = timezone.now() - timedelta(days=90)
        user_orders = UserOrder.objects.filter(
            order__order_products__product=obj,
            datetime__gte=three_months_ago
        )

        # Group by month
        user_orders_by_month = defaultdict(int)
        for user_order in user_orders:
            month = user_order.datetime.strftime('%B')
            user_orders_by_month[month] += 1

        # Format the result
        history = []
        for month, count in user_orders_by_month.items():
            history.append({
                'month': month,
                'count':count
            })

        return history