from django.shortcuts import render, redirect
from Tienda.models import Producto
from .CarroCompra import CarroCompra
# Create your views here.

def agregar_producto(request, producto_id):
    carro = CarroCompra(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)

    return redirect("/tienda")

def eliminar_producto(request, producto_id):
    carro = CarroCompra(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)

    return redirect("/tienda")

def restar_producto(request, producto_id):
    carro = CarroCompra(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)

    return redirect("/tienda")

def limpiar_carro(request):
    carro = CarroCompra(request)
    carro.vaciar()

    return redirect("/tienda")
    
