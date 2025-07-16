from django.db import models
from sqlalchemy import delete


# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Profile for: {self.user.username}"
    

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
