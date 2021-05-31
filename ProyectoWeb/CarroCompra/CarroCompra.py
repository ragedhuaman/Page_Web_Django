class CarroCompra:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro =self.session.get("carro")

        if not carro:
           self.carro = self.session["carro"] ={}
        else:
           self.carro = carro

    def agregar(self, producto):
        
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                    "producto_id":producto.id,
                    "nombre":producto.nombre,
                    "precio":str(producto.precio),
                    "cantidad":1,
                    "imagen":producto.img.url,
                    "costo_total":str(producto.precio)
                }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] +=1
                    value["costo_total"] = float(value["precio"])*value["cantidad"]
                    break
        
        self.guardar()

    def restar(self, producto):
    
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -=1
                if value["cantidad"]<=0:
                    self.eliminar(producto)
                break

        self.guardar()

    def eliminar(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.carro.keys():
            del self.carro[producto_id]
            self.guardar()
    
    def vaciar(self):
        self.carro = self.session["carro"] = {}
        self.session.modified = True


    def guardar(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    
