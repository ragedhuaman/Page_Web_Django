from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formContacto
from  django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario = formContacto()
    estado = False
    if request.method =="POST":
        formulario = formContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            email = EmailMessage('Mensaje desde App Django',f'''El usuario {nombre} con la 
            direccion de correo {email} escribe lo siguiente:\n\n {contenido}''',"",['raged.huaman@unmsm.edu.pe'],reply_to=[email])
            try:
                email.send()
                return redirect('/contacto/?valido') 
            except:
                return redirect('/contacto/?novalido')

    return render(request, 'Contacto/contacto.html',{"miFormulario":formulario})


