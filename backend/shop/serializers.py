from rest_framework import serializers
from .models import User

class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','fullname','phonenumber']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            fullname=validated_data['fullname'],
            phonenumber=validated_data['phonenumber']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        