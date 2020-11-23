from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('you are at /blog')

def blog(request, blogid):
    return HttpResponse('you are at /blog/%i' % blogid)
