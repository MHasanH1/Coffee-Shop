from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework import status
from .serializers import UserCreationSerializer,ProductSerializer,OrderProductSerializer,OrderSerializer,UserSerializer,StorageSerializer,UserOrderSerializer,CustomProductSerializer
from .models import Vertical,Product,UserOrder,Order,OrderProduct,User,Storage
from rest_framework.decorators import api_view,permission_classes
from django.db.models import Count
from datetime import datetime


class RegisterView(APIView):
    def post(self, request :Request, *args, **kwargs):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            print(created)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ShowProductsByVerticals(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request:Request):
        i=request.data.get('ver')
        products=Product.objects.filter(vertical=i)
        products_by_vertical = ProductSerializer(products,many=True,context={"request":request}).data
        return Response(products_by_vertical)
    

class ProductView(APIView):
    def post(self,request:Request):
        serializer = ProductSerializer(data=request.data,context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

    
    

class AddToCartView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request:Request,product_id:int):
        is_active_user_order=UserOrder.objects.filter(user=request.user,is_active=True).exists()
        if is_active_user_order:
            user_order=UserOrder.objects.filter(user=request.user,is_active=True).last()
        else:
            order=Order.objects.create()
            user_order=UserOrder.objects.create(user=request.user,order=order)
        order=user_order.order
        print(product_id)
        product=Product.objects.get(id=product_id)

        order_product=OrderProduct.objects.create(order=order,product=product)
        checked=order_product.check_product()
        if checked[0]:

            # order_product.count+=1
            # order_product.save()
            sugar_storage=Storage.objects.get(name="sugar")
            coffee_storage=Storage.objects.get(name="coffee")
            flour_storage=Storage.objects.get(name="flour")
            sugar_storage.amount-= order_product.product.sugar
            coffee_storage.amount-= order_product.product.coffee
            flour_storage.amount-= order_product.product.flour
            sugar_storage.save()
            coffee_storage.save()
            flour_storage.save()
            print(f"sugar {sugar_storage.amount}")
            serialized=OrderProductSerializer(order_product,context={"request":request})
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        else:

            order_product.delete()
            return Response(data={"message":f"not enough storage for {checked[1]}"},status=status.HTTP_406_NOT_ACCEPTABLE)
            
        #     return Response(serialized.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response({"message":"already exists in cart"},status=status.HTTP_302_FOUND)
        



        

class CartView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request:Request):
        user_order=UserOrder.objects.filter(user=request.user,is_active=True).last()
        # products=Product.objects.filter(order_products__order=user_order.order)
        if user_order is None:
            return Response(data=None,status=status.HTTP_200_OK)
        print(user_order.order)
        serialized = OrderSerializer(user_order.order,many=False,context={"request":request}).data

        return Response(data=serialized,status=status.HTTP_200_OK)


class OrderView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request:Request):
        orders=UserOrder.objects.filter(user=request.user,is_active=False)
        serialized=UserOrderSerializer(orders,many=True,context={"request":request})
        
        return Response(data=serialized.data,status=status.HTTP_200_OK)

        
class LogoutView(APIView):
    def post(self, request):
        token = request.auth
        if token:
            Token.objects.filter(key=token).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def authentication(request:Request):
    return Response(status=status.HTTP_200_OK)


class PopularView(APIView):
    def get(self,request:Request):
            top_products = (Product.objects
                    .annotate(order_count=Count('order_products'))
                    .order_by('-order_count')[:12])
            
            serialized=ProductSerializer(top_products,many=True,context={"request":request})
            return Response(serialized.data,status=status.HTTP_200_OK)
    


class ProfileView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request:Request):
        print(request.user.id)
        user=User.objects.get(id=request.user.id)
        serialized=UserSerializer(user).data
        return Response(serialized,status=status.HTTP_200_OK)


class RemoveFromCart(APIView):
    def post(self,request:Request):
        product_id=request.data.get('id')
        product=Product.objects.get(id=product_id)
        order=UserOrder.objects.filter(user=request.user,is_active=True).last().order
        order_product=OrderProduct.objects.filter(order=order,product=product).first()
        sugar_storage=Storage.objects.get(name="sugar")
        coffee_storage=Storage.objects.get(name="coffee")
        flour_storage=Storage.objects.get(name="flour")
        if order_product:
            sugar_storage.amount+= order_product.product.sugar
            coffee_storage.amount+= order_product.product.coffee
            flour_storage.amount+= order_product.product.flour
            sugar_storage.save()
            coffee_storage.save()
            flour_storage.save()
            order_product.delete()
            print(f"sugar {sugar_storage.amount}")
            return Response({"message":"deleted"},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class SupplyView(APIView):
    def post(self,request:Request):
        try:
            storage=Storage.objects.get(name=request.data.get('name'))
            storage.amount=request.data.get('amount')

            storage.save()
            serializer=StorageSerializer(storage,many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,requst:Request):
        storage=Storage.objects.all()
        serializer=StorageSerializer(storage,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class ConfirmCartView(APIView):
    def get(self,request:Request):
        user_order=UserOrder.objects.filter(user=request.user,is_active=True).last()
        user_order.is_active=False
        user_order.datetime=datetime.now()
        user_order.save()
        serializer= UserOrderSerializer(user_order,context={"request":request})
        return Response(serializer.data,status.HTTP_200_OK)
    


class ChartView(APIView):
    def get(self,request:Request):
        products=Product.objects.all()
        serializer=CustomProductSerializer(products,many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    



