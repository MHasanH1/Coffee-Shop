from rest_framework import serializers
from .models import User

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

        