from django.http import HttpResponse
from django.shortcuts import redict

def index(request):
    return HttpResponse('index')

def login(request):
    return redict('/index')
