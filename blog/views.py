from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogPost

# blog index page
def index(request):
    context = {
        'blogs': BlogPost.objects.all(), # all blogs
        'recent_blogs': BlogPost.objects.order_by('-date')[:5], # top 5 most recent blogs
    }
    return render(request, 'blog/index.html', context)

# view a blog (blogid -> blog)
def blog(request, blogid):
    context = {
        'blog': BlogPost.objects.get(pk=blogid),
    }
    return render(request, 'blog/blog.html', context)
