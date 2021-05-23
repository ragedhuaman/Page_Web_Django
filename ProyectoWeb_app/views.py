from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'ProyectoWeb_app/home.html')

def servicios(request):
    return render(request, 'ProyectoWeb_app/servicios.html')

def tienda(request):
    return render(request, 'ProyectoWeb_app/tienda.html')

def blog(request):
    return render(request, 'ProyectoWeb_app/blog.html')

def contacto(request):
    return render(request, 'ProyectoWeb_app/contacto.html')
