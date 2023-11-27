from  .views import add_user, get_users, hello, calc, login
from django.urls import path

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
    path('users', get_users),
    path('add_user', add_user),
    path('login', login),
]