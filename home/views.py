from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from product.models import Product
from blog.models import Blog
from .forms import ContactForm


# Create your views here.

def home(request):
    products = Product.objects.all().order_by('-id')[:8]
    blogs = Blog.objects.all().order_by('-id')[:3]
    context = {'products': products, "blogs": blogs}
    return render(request, 'home/home.html', context)


def about_us(request):
    return render(request, 'home/about_us.html')


def faq(request):
    return render(request, 'home/faq.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"},safe=False)
        else:
            context = {"errors": form.errors}
            return JsonResponse(context,safe=False)


def search(request):
    search_key = request.GET.get('search')
    product_result = Product.objects.filter(Q(name__icontains=search_key) | Q(search_key__icontains=search_key))
    p = Paginator(product_result, 8)
    page_number = request.GET.get('page', 1)
    try:
        page = p.page(page_number)
    except:
        page = p.page(1)
    context = {'products': page, "page_number": page_number, 'search_key': search_key}
    return render(request, 'home/search.html', context)


def search_cat(request, str):
    search_key = str
    if search_key == "all":
        product_result = Product.objects.all()
    else:
        product_result = Product.objects.filter(category__name=search_key)
    p = Paginator(product_result, 8)
    page_number = request.GET.get('page', 1)
    try:
        page = p.page(page_number)
    except:
        page = p.page(1)
    context = {'products': page, "page_number": page_number, 'search_key': search_key, "cat": str}
    return render(request, 'product/product.html', context)
