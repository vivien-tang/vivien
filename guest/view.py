from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello Django!")
def index1(request):
    return HttpResponse("Hello Django!")