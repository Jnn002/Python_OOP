# Ejemplo 2, Composition

class Motor:
    def __init__(self, caballos_fuerza):
        self.caballos_fuerza = caballos_fuerza

class Llantas:
    def __init__(self, rin):
        self.rin = rin
        

class Carro:
    def __init__(self, modelo, caballos_fuerza, rin_llanta):
        self.modelo = modelo
        
        self.caballos_fuerza = Motor(caballos_fuerza)
        self.rin_llanta = Llantas(rin_llanta)
    
    # Método para mostrar los detalles del carro
    def detalles_carro(self):
        return f"Modelo: {self.modelo}\nCaballos de fuerza: {self.caballos_fuerza.caballos_fuerza}\nRin: {self.rin_llanta.rin}"
        
pick_up = Carro('Ford', 300, 22)
carrito = Carro('Toyota', 200, 18)

print(pick_up.detalles_carro())
print(carrito.detalles_carro())
# Manera para imprimir un atributo de un objeto dentro de otro objeto
print(carrito.rin_llanta.rin)