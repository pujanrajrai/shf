from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.blogs, name='all_blogs'),
    path('details/<slug:slug>/', views.blog_details, name='blog_details'),
]
