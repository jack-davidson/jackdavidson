from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost

# blog homepage
def index(request):
    return HttpResponse('you are at /blog')

# return most recently posted blog
def blog(request, blogid):
    return HttpResponse(BlogPost.objects.order_by('-date')[0]);
