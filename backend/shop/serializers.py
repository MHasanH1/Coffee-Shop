from rest_framework import serializers
from .models import User,Product,OrderProduct,UserOrder,Order

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
        order_products=OrderProduct.objects.filter(order=cart.order,product=obj)
        return order_products.count()

        
    

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