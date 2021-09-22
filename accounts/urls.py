"""furniture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [
    # path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path("activate-user/<uidb64>/<token>", views.activate_user, name="activate"),
    path('logout/', views.logout, name='logout'),
    # path('oauth/', include('social_django.urls', namespace='social')),
    # path('loggedin/', views.loggedin,name='logged_in'),

]
