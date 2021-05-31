from django.urls import path
from. import views


urlpatterns = [
    path('tienda', views.tienda, name = 'Tienda'),
    path('tienda/categoria/<categoria_id>', views.ProductoByCategoria, name = 'ProductoByCategoria')
]
#Darle a Django la ruta para encontrar la imagen
