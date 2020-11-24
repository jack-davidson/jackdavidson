from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost

# blog homepage
def index(request):
    context = {
        'blogs': BlogPost.objects.all(),
    }
    return render(request, 'blog/index.html', context)

# return most recently posted blog
def blog(request, blogid):
    context = {
        'blog': BlogPost.objects.get(pk=blogid),
    }
    return render(request, 'blog/blog.html', context);
