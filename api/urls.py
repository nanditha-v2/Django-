from django.urls import path
from .views import get_user, CREATE_user

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', CREATE_user, name='create_user')
]
