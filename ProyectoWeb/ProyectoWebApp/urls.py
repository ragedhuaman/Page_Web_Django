from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name = 'Home'),
]
#Darle a Django la ruta para encontrar la imagen
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)