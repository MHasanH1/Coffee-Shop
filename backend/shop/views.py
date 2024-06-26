from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from rest_framework import status
from .serializers import UserCreationSerializer,ProductSerializer,OrderProductSerializer,OrderSerializer
from .models import Vertical,Product,UserOrder,Order,OrderProduct


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
    def get(self,request:Request):
        i=request.data.get('ver')
        products=Product.objects.filter(vertical=i)
        products_by_vertical = ProductSerializer(products,many=True).data
        return Response(products_by_vertical)
    

class ProductView(APIView):
    def post(self,request:Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AddToCartView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request:Request,product_id:int):
        is_active_user_order=UserOrder.objects.filter(is_active=True).exists()
        if is_active_user_order:
            user_order=UserOrder.objects.filter(is_active=True).last()
        else:
            order=Order.objects.create()
            user_order=UserOrder.objects.create(user=request.user,order=order)
        order=user_order.order
        print(product_id)
        product=Product.objects.get(id=product_id)
        order_product,created=OrderProduct.objects.get_or_create(order=order,product=product)
        serialized=OrderProductSerializer(order_product,context={"request":request})
        if created:
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"already exists in cart"},status=status.HTTP_302_FOUND)
        

    def get(self,request:Request):
        orders=Order.objects.filter(user_orders__user=request.user)
        serialized=OrderSerializer(orders,many=True)
        return Response(data=serialized.data,status=status.HTTP_200_OK)

        
class LogoutView(APIView):
    def post(self, request):
        token = request.auth
        if token:
            Token.objects.filter(key=token).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
