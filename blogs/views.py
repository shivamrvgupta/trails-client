from .models import Blog,Newsletter
from django.shortcuts import render, redirect

# Create your views here.


def blogs(request):
    blogs = Blog.objects.order_by('-date').filter(is_published=True)
    
    context = {
        'blogs' : blogs
    }

    return render(request, 'products/blogs-list.html',context)

