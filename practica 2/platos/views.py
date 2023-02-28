from django.shortcuts import render
from django.http import HttpResponse
from .models import Platos
# Create your views here.
def platos_list(request):
    #platos = Platos.objects.all()

    platillos = Platos.objects.filter(procedencia='Perú',precio__gte=40)
    return render(request, 'platos/platos_list.html', context={'data': platos})