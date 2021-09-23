from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm
from .models import Blog, Comment


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
    context = {}
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog__slug=slug).filter(active=True)
    comment_count = Comment.objects.filter(blog__slug=slug).filter(active=True).count()
    comment_form = CommentForm()
    if request.method == 'POST':
        forms = CommentForm(request.POST)
        if forms.is_valid():
            Comment.objects.create(
                blog=Blog.objects.get(slug=slug),
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                body=request.POST.get('body'),
            )
            print(000)
            return redirect(f'/blogs/details/{slug}')

        else:
            print(1)
            print(forms.errors)
            context['errors'] = forms.errors
    context['blogs'] = blog
    context['slug'] = slug
    context["comment_form"] = comment_form
    context["comments"] = comments
    context["comment_count"] = comment_count
    return render(request, 'blog/blog_details.html', context)
