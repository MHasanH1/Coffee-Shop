from django.shortcuts import render

# Create your views here.

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from .serializers import UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request:Request):
        # Your authentication logic here
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
