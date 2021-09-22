from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.all_product, name='all_product'),
    path('details/<slug:slug>/', views.product_details, name='product_details'),
    path('inquiry/', views.product_inquiry, name='product_inquiry')

]
