from rest_framework import serializers
from .models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__' 


class UserSerializer(serializers.ModelSerializer):
     profile = UserProfileSerializer(read_only=True)

     class Meta:
        model = User
        fields = '__all__'

