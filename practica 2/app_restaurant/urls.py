from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meseros/',include('meseros.urls')),
    path('platillos/',include('platos.urls')),
]
