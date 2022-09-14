from rest_framework.serializers import ModelSerializer
from .models import *

class T_UserSerializer(ModelSerializer):
    class Meta:
        model = T_User
        fields = '__all__'

class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'