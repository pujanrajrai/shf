from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog


# Create your views here.

def blogs(request):
    blog = Blog.objects.all().order_by('-id')
    p = Paginator(blog, 8)
    page_number = request.GET.get('page', 1)
    try:
        page = p.page(page_number)
    except:
        page = p.page(1)
    context = {'blogs': page, "page_number": page_number}
    return render(request, 'blog/blog.html', context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {'blogs': blog, 'slug': slug}
    return render(request, 'blog/blog_details.html', context)
