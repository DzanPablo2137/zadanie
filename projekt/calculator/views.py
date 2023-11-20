from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse

def hello(request, number):
    print(request)
    return HttpResponse(f"Hello, Django!  {number}")

@csrf_exempt
def calc(request):
    return HttpResponse(f"")