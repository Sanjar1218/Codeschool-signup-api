from django.db import models
from django.contrib.auth.models import User 

class T_User(models.Model):
    t_first_name = models.CharField(max_length=100)
    t_username = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.t_first_name

class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    option = models.TextField(max_length=200)
    user = models.OneToOneField(T_User, on_delete=models.CASCADE)