from django.urls import path
from. import views


urlpatterns = [
    path('agregar/producto/<producto_id>', views.agregar_producto, name = 'Agregar'),
    path('restar/producto/<producto_id>', views.restar_producto, name = 'Restar'),
    path('eliminar/producto/<producto_id>', views.eliminar_producto, name = 'Eliminar'), 
    path('limpiar', views.limpiar_carro, name = 'Limpiar') 
]