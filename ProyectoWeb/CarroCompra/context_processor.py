from .CarroCompra import CarroCompra

#VARIABLE GLOBAL DEL PROYECTO

def importe_total_carro(request):
    carro=CarroCompra(request)
    total=0
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total +=float(value["precio"])*value["cantidad"]

    return{"importe_total_carro":total}

def calcular_suma(request):
    if request.user.is_authenticated:
        return {"calcular_suma":5}

