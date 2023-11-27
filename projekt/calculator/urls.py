from  .views import get_users, hello, calc
from django.urls import path

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users),
]