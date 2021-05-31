from django.shortcuts import render
from .models import CategoriaProducto, Producto
# Create your views here.
def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.all()
    return render(request, 'Tienda/tienda.html',{"productos":productos, "categorias":categorias})

def ProductoByCategoria(request,categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    return render(request, 'Tienda/ProductoByCategoria.html',{"productos":productos,"categoria":categoria})