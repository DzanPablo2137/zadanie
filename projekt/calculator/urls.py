from  .views import hello, calc
from django.urls import path

urlpatterns = [
    path('hello/<int:number>', hello),
    path('calc', calc),
]