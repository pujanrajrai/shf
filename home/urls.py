from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('faq/', views.faq, name='faq'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('search/categories/<str:str>',views.search_cat,name='search_cat'),
]
