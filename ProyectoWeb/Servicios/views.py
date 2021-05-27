from django.shortcuts import render
from .models import Servicio
# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'Servicios/servicios.html',{"servicios":servicios})