from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def index(request):
    return HttpResponse('Success')
