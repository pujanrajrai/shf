import re
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
# from django.urls import reverse
from home.models import Contact
from product.models import Category, Product, ProductImage, ProductInquiry
from .forms import ProductForms, BlogForms, CategoryForm
from product.models import Category
from blog.models import Blog
from django.contrib import messages


# Create your views here.
@staff_member_required()
def product_create(request):
    context = {}
    categories = Category.objects.all()
    form = ProductForms()
    if request.method == 'POST':
        content = request.POST['desc']
        clean = re.compile('<.*?>')  # identifying HTML tags
        cleaned_data = re.sub(clean, '', content)  # removing HTML tags
        cleaned_data = cleaned_data.replace("&nbsp;", " ")  # removing '&nbsp;'
        name = request.POST['name']
        category = request.POST['category']
        search_key = request.POST['search_key']
        data = {"name": name, "desc": cleaned_data, "category": category, "search_key": search_key}
        forms = ProductForms(data, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard:product')
        else:
            context["errors"] = forms.errors
    context["categories"] = categories
    context["form"] = form
    return render(request, 'dashboard/add_product.html', context)


@staff_member_required()
def product_update(request, slug):
    context = {}
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    form = ProductForms(instance=product)
    product_images = ProductImage.objects.filter(product__name=product)
    if request.method == 'POST':
        content = request.POST['desc']
        clean = re.compile('<.*?>')  # identifying HTML tags
        cleaned_data = re.sub(clean, '', content)  # removing HTML tags
        cleaned_data = cleaned_data.replace("&nbsp;", " ")  # removing '&nbsp;'
        name = request.POST['name']
        category = request.POST['category']
        search_key = request.POST['search_key']
        data = {"name": name, "desc": cleaned_data, "category": category, "search_key": search_key}
        forms = ProductForms(data, request.FILES, instance=product)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard:product')
        else:
            context["errors"] = forms.errors
    context["categories"] = categories
    context["form"] = form
    context['product'] = product
    context['product_images'] = product_images
    return render(request, 'dashboard/update_product.html', context)


@staff_member_required()
def product_view(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'dashboard/product.html', context)


@staff_member_required()
def remove_product(request, id):
    if request.method == "POST":
        Product.objects.filter(id=id).delete()
        return redirect('dashboard:product')
    return redirect('dashboard:product')


@staff_member_required()
def blog_view(request):
    blog = Blog.objects.all()
    context = {'blog': blog}
    return render(request, 'dashboard/blog.html', context)


@staff_member_required()
def blog_create(request):
    forms_field = BlogForms()
    context = {"forms": forms_field}
    if request.method == 'POST':
        content = request.POST['desc']
        clean = re.compile('<.*?>')
        cleaned_data = re.sub(clean, '', content)  # removing HTML tags
        cleaned_data = cleaned_data.replace("&nbsp;", " ")  # removing '&nbsp;'
        name = request.POST['name']
        category = request.POST['category']
        data = {"name": name, "desc": cleaned_data, "category": category}
        forms = BlogForms(data, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard:blog')
        else:
            context["errors"] = forms.errors
    return render(request, 'dashboard/add_blog.html', context)


@staff_member_required()
def blog_update(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    forms_field = BlogForms(instance=blog)
    context = {"forms": forms_field, "slug": slug, "blog": blog}
    if request.method == 'POST':
        content = request.POST['desc']
        clean = re.compile('<.*?>')
        cleaned_data = re.sub(clean, '', content)  # removing HTML tags
        cleaned_data = cleaned_data.replace("&nbsp;", " ")  # removing '&nbsp;'
        name = request.POST['name']
        category = request.POST['category']
        data = {"name": name, "desc": cleaned_data, "category": category}
        forms = BlogForms(data, request.FILES, instance=blog)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard:blog')
        else:
            context["errors"] = forms.errors
    return render(request, 'dashboard/blog_update.html', context)


@staff_member_required()
def remove_blog(request, id):
    if request.method == "POST":
        Blog.objects.filter(id=id).delete()
        return redirect('dashboard:blog')
    return redirect('dashboard:blog')


@staff_member_required()
def dashboard(request):
    total_product = Product.objects.all().count()
    total_blog = Blog.objects.all().count()
    total_inquiry = ProductInquiry.objects.all().count()
    total_contact = Contact.objects.all().count()
    total_product_category = Category.objects.all().count()
    context = {
        "total_product": total_product,
        "total_blog": total_blog,
        "total_inquiry": total_inquiry,
        "total_contact": total_contact,
        "total_product_category": total_product_category
    }
    return render(request, 'dashboard/home.html', context)


@staff_member_required()
def categories(request):
    category = Category.objects.all()
    context = {"categories": category}
    return render(request, 'dashboard/category.html', context)


@staff_member_required()
def cat_add(request):
    context = {}
    if request.method == 'POST':
        forms = CategoryForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard:categories')
        else:
            context["errors"]= forms.errors
    return render(request, 'dashboard/category_add_update.html', context)


@staff_member_required()
def contact_details(request):
    contact = Contact.objects.all()
    context = {"contact": contact}
    return render(request, 'dashboard/contact.html', context)


@staff_member_required()
def contact_specific_details(request, slug):
    contact = Contact.objects.filter(message_viewed=slug)
    context = {"contact": contact}
    return render(request, 'dashboard/contact.html', context)


@staff_member_required()
def contact_read(request, str):
    contact = Contact.objects.filter(id=str).update(message_viewed=True)
    return redirect("/dashboard/contact/False")


@staff_member_required()
def inquiry(request):
    inquiry = ProductInquiry.objects.all()
    context = {'inquiry': inquiry}
    return render(request, 'dashboard/inquiry.html', context)


def inquiry_specific_details(request, slug):
    inquiry = ProductInquiry.objects.filter(viewed=slug)
    context = {'inquiry': inquiry}
    return render(request, 'dashboard/inquiry.html', context)


def inquiry_read(request, str):
    inquiry = ProductInquiry.objects.filter(id=str).update(viewed=True)
    return redirect("dashboard:inquiry")
