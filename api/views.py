from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import T_User, Data
from .serializers import DataSerializer, T_UserSerializer

@api_view(['post'])
def add_data(request):
    data = request.data
    # user = T_UserSerializer(data=request.data)
    # data = DataSerializer(data=request.data['data'])

    if not T_User.objects.filter(t_first_name=data.get('t_first_name', '')).exists():
        instance = T_User(t_first_name=data.get('t_first_name', ''), t_username=data.get('t_username', ''))
        info = data['data']
        ins = Data(first_name=info.get('first_name',''), last_name=info.get('last_name', ''), email=info.get('email', ''), option=info.get('option',''), user=instance)

        instance.save()
        ins.save()
        return Response({'status':'user added'}, status=200)
    else:
        return Response({'status':'user is exist'})

@api_view(['get'])
def get_data(request):
    q = request.data.get('username', '')
    lst = T_User.objects.filter(t_first_name__icontains=q)
    users = []
    for i in lst:
        dct = {}
        dct['t_first_name'] = i.t_first_name
        dct['t_username'] = i.t_username
        dct['data'] = {}
        dct['data']['first_name'] = i.data.first_name
        dct['data']['last_name'] = i.data.last_name
        dct['data']['email'] = i.data.email
        dct['data']['option'] = i.data.option
        users.append(dct)
    return Response(users)

@api_view(['delete'])
def remove_user(request):
    q = request.data.get('first_name', '')
    user = T_User.objects.filter(t_first_name=q)
    if user.count()==1:
        user.delete()
        return Response({'status': 'User deleted'})
    else:
        return Response({'status': 'User is not exists'})
