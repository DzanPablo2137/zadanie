from  .views import hello
from django.urls import path

urlpatterns = [
    path('hello/<int:number>', hello),
]