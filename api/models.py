from django.db import models
from django.contrib.auth.models import User 

class T_User(models.Model):
    t_first_name = models.CharField(max_length=100)
    t_username = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    option = models.TextField(max_length=200)
    user = models.OneToOneField(T_User, on_delete=models.CASCADE)