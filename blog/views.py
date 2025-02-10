from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.db.models import Count

# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'blogs': blogs})

def blogpost(request, slug):  # ✅ Accept `slug` as a function parameter
    blog = get_object_or_404(Blog, slug=slug)  # ✅ Filter the blog using slug
    blog.views += 1
    blog.save()
    top_blogs = Blog.objects.all().order_by('-views')[:3]
    related_blogs = Blog.objects.filter(category = blog.category).exclude(slug=slug)[:3]
    previous_blog = Blog.objects.filter(created_at__lt=blog.created_at).first()
    next_blog = Blog.objects.filter(created_at__gt=blog.created_at).first()
    categories = Category.objects.annotate(post_count=Count('blog'))
    return render(request, 'blog/single_blog.html', {'blog': blog, 
                                                     'related_blogs': related_blogs, 
                                                     'previous_blog': previous_blog, 
                                                     'next_blog': next_blog,  
                                                     'categories': categories,
                                                     'top_blogs' : top_blogs})

def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    return render(request, 'category.html', {'category': category})


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')