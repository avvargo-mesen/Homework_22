from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Blog

# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blogs'
