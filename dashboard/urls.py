from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('product/create/', views.product_create, name='product_create'),
    path('blog/create/', views.blog_create, name='create_blog'),
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.cat_add, name='cat_add'),
    path('blogs/', views.blog_view, name='blog'),
    path('blogs/update/<slug:slug>', views.blog_update, name='blog_update'),
    path('product/', views.product_view, name='product'),
    path('product/delete/<str:id>', views.remove_product, name='product_remove'),
    path('blog/delete/<str:id>', views.remove_blog, name='blog_remove'),
    path('product/update/<slug:slug>', views.product_update, name='product_update'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('inquiry/<slug:slug>', views.inquiry_specific_details, name='inquiry_specific'),
    path('inquiry/read/<str:str>', views.inquiry_read, name='inquiry_read'),
    path('contact/', views.contact_details, name='contact'),
    path('contact/<slug:slug>', views.contact_specific_details, name='contact_specific'),
    path('contact/read/<str:str>', views.contact_read, name='contact_read'),
]
