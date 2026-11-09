from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import Blog

# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blogs_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self):
        obj = super().get_object()
        obj.views_count +=1
        obj.save()

        return obj

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/blog_create.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/blog_create.html'
    context_object_name = 'blog'

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/confirm_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blog:blog_list')

