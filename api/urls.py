from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_user, name='get_user'),
    path('users/create/', views.CREATE_user, name='create_user'),
    path('userprofiles/', views.get_user_profiles, name='get_user_profiles'),
    path('userprofiles/create/', views.create_user_profile, name='create_user_profile'),
    path('tasks/', views.task_list, name='get_tasks'), 
    path('tasks/create/', views.task_list, name='create_task'),  
]

