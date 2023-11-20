from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request, number):
    print(request)
    return HttpResponse(f"Hello, Django!  {number}")

def calc(request):
    pass