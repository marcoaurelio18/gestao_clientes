from django.contrib import admin
from django.urls import path, include
from clientes import urls as clientes_urls
from home import urls as home_urls

# URLs principais do sistema
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('clientes/', include(clientes_urls)),
    path('', include('django.contrib.auth.urls')),
]
