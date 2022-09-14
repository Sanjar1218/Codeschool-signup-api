from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import DataSerializer, T_UserSerializer

@api_view(['get', 'post'])
def add_data(request):
    user = T_UserSerializer(data=request.data)
    data = DataSerializer(data=request.data['data'])
    if user.is_valid():
        print(user.data)
        # user.save()
    if data.is_valid():
        print(data.data)
    return Response(request.data)
