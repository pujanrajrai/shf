from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Product, ProductInquiry
from .forms import ProductInquiryForm
from django.contrib import messages


# Create your views here.

def all_product(request):
    products = Product.objects.all()
    p = Paginator(products, 8)
    page_number = request.GET.get('page', 1)
    try:
        page = p.page(page_number)
    except:
        page = p.page(1)
    context = {'products': page, "page_number": page_number}
    return render(request, 'product/product.html', context)


def product_details(request, slug):
    context = {}
    product = Product.objects.get(slug=slug)
    related_product = Product.objects.filter(category__name=product.category).order_by('-id')[:4]
    if request.method == 'POST':
        slug = request.POST.get('slug')
        form = ProductInquiryForm(request.POST)
        if form.is_valid():
            ProductInquiry.objects.create(
                product=Product.objects.get(slug=slug),
                name=request.POST.get('name'),
                phone_number=request.POST.get('phone_number'),
                address=request.POST.get('address'),
                quantity=request.POST.get('quantity'),
            )
            messages.success(request, 'Inquiry send successfully ')

            return redirect('product:product_details', slug=slug)
        else:
            context['errors'] = form.errors
            print(context)
    context['product'] = product
    context['related_product'] = related_product
    context["slug"] = slug
    return render(request, 'product/product_details.html', context)


def product_inquiry(request):
    context = {}
    if request.method == 'POST':
        slug = request.POST.get('slug')
        form = ProductInquiryForm(request.POST)
        if form.is_valid():
            ProductInquiry.objects.create(
                product=Product.objects.get(slug=slug),
                name=request.POST.get('name'),
                phone_number=request.POST.get('phone_number'),
                address=request.POST.get('address'),
                quantity=request.POST.get('quantity'),
            )
            return redirect('product:product_details', slug=slug)
        else:
            context['errors'] = form.errors
        return render(request, 'product/product_details.html')
