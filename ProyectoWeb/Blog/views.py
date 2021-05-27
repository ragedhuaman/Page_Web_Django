from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'Blog/blog.html',{"posts":posts, "categorias":categorias})

def postByCategoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, 'Blog/blog_categoria.html',{"posts":posts,"categoria":categoria})