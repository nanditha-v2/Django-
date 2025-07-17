from rest_framework import serializers
from .models import User, UserProfile, Task

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'phone', 'address', 'birth_date']



class TaskSerializer(serializers.ModelSerializer):
    class meta:
        model=Task
        fields= '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    tasks = TaskSerializer( many=True, read_only=True)
   
    class Meta:
        model = User
        fields = ['id', 'age', 'name', 'profile', 'tasks']
    
