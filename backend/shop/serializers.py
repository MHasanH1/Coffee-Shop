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
    # vertical = serializers.CharField(source='vertical.label')
    class Meta:
        model=Product
        fields=('name','sugar','coffee','flour','vertical','price')
    
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
    

class OrderProductSerializer(serializers.ModelSerializer):
    is_ordered_now=serializers.SerializerMethodField()
    class Meta:
        model = OrderProduct
        fields=('id','product','order','is_ordered_now')

    def get_is_ordered_now(self,obj:OrderProduct):
        user=self.context['request'].user
        return UserOrder.objects.filter(user=user,order=obj.order).last().is_active
    

    

class OrderSerializer(serializers.ModelSerializer):
    products=serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields=('id','products','purchase_amount','type')
    
    def get_products(self,obj:Order):
        products=Product.objects.filter(order_products__order=obj)
        return ProductSerializer(products,many=True).data