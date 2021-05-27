from django.urls import path
from. import views


urlpatterns = [
    path('tienda', views.tienda, name = 'Tienda'),
]
#Darle a Django la ruta para encontrar la imagen
