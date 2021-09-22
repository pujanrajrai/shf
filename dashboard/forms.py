from django import forms
from product.models import Product, Category, ProductImage
from blog.models import Blog


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "desc",
            "category",
            "thumbnail_image",
            "thumbnail_image2",
            "search_key",
            "product_images1",
            "product_images2",
        ]


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
            "desc",
        ]


class ProductImageForms(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = [
            "product",
            "product_image",
        ]


class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            "name",
            "desc",
            "thumbnail_image",
            "category"
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'desc']
