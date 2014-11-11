from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Show me the money!!!")

def order(request, diner_id):
    return HttpResponse(open("../www/index.html").read())

def js_file(request, file_name):
    return HttpResponse(open("../www/" + file_name + ".js").read())

def css_file(request, file_name):
    return HttpResponse(open("../www/" + file_name + ".css").read())