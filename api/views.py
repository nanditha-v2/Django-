from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task, User
from .serializer import TaskSerializer, UserSerializer
from .models import UserProfile
from .serializer import UserProfileSerializer

@api_view(['GET'])
def get_user(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CREATE_user(request):
     serializer = UserSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
     try:
          user = User.objects.get(pk=pk)
     except User.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
     

     if request.method == 'GET':
          serializer = UserSerializer(user)
          return Response(serializer.data)
     
     if request.method == 'PUT':
          serializer = UserSerializer(user, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     if request.method == 'DELETE':
          user.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
                         
     

@api_view(['GET'])
def get_user_profiles(request):
     profiles = UserProfile.objects.all()
     serializer = UserProfileSerializer(profiles, many=True)
     return Response(serializer.data)

@api_view(['POST'])
def create_user_profile(request):
     serializer = UserProfileSerializer(data=request.data)
     if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def task_list(request):
     if request.method == 'GET':
          tasks = Task.objects.all()
          serializer = TaskSerializer(tasks, many=True)
          return Response({"msg": "Task Data", "data": serializer.data}, status=200)
     
     elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            task_data = {
                'user': user_instance.id,
                'title': request.data.get('title'),
                'description': request.data.get('description'),
                'due_date': request.data.get('due_date')
            }

            task_serializer = TaskSerializer(data=task_data)

            if task_serializer.is_valid():
                task_serializer.save()
                return Response({"msg": "User and Task saved successfully"}, status=201)
            else:
                  user_instance.delete()
                  return Response({"msg": "Task not saved", "errors": task_serializer.errors}, status=400)

        else:
            return Response({"msg": "User data invalid", "errors": user_serializer.errors}, status=400)
