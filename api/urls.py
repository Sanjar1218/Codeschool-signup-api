from django.urls import path
from .views import add_data, get_data, remove_user

urlpatterns = [
    path('add', add_data, name='add'),
    path('users', get_data, name='get'),
    path('remove', remove_user, name='remove')
]
