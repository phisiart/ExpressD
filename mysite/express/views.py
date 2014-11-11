from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Show me the money!!!")

def order(request, diner_id):
    return HttpResponse("order" + diner_id)