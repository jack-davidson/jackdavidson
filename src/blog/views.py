from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import BlogPost


# blog index page
def index(request):
    # unorded list of all blogs
    blogs = BlogPost.objects.all()

    # ordering the blogs list and taking the top 5 most recent
    recent_blogs = blogs.order_by('-date')[:5]

    # context stores the variables our template needs access to
    context = {
        'blogs': blogs,                # all blogs
        'recent_blogs': recent_blogs,  # top 5 most recent blogs
    }

    return render(request, 'blog/index.html', context)


# view a blog by its id
def blog(request, blogid):
    # handle the case of a nonexistent requested blog
    try:
        blog = BlogPost.objects.get(pk=blogid)
    except ObjectDoesNotExist:
        blog = None

    # context stores the variables our template needs access to
    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)
