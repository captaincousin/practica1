from django.urls import path
from . import views

urlpatterns =[
    path('platillos_list', views.platillos_list, name='platillos_list')
]