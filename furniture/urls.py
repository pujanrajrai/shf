from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('dashboard/', include('dashboard.urls')),
                  path('blogs/', include('blog.urls')),
                  path('products/', include('product.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
