from django.shortcuts import render
import os

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(open('index.html').read())

def order(request, diner_id):
    return HttpResponse(open("dashboard.html").read())

def js_file(request, file_name):
    return HttpResponse(open(file_name + ".js").read())

def css_file(request, file_name):
    return HttpResponse(open(file_name + ".css").read())