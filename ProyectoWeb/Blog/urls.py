from django.urls import path
from . import views


urlpatterns = [
    path('blog', views.posts, name = 'Blog'),
    path('blog/categoria/<categoria_id>', views.postByCategoria, name = 'PostByCategoria')
]

















