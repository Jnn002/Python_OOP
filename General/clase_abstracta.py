# Clase abstraca
# Una clase abstracta es una clase que no puede ser instanciada. 
# Es decir, no podemos crear objetos de una clase abstracta.

from abc import ABC, abstractmethod

class Vehiculo(ABC):
# ESTA CLASE Y SUS METODOS SON ABSTRACTOS
# NO SE PUEDEN INSTANCIAR DIRECTAMENTE
    @abstractmethod
    def avanzar(self):
        pass

    @abstractmethod
    def parar(self):
        pass
# Clase hija
class Moto(Vehiculo):
    # Implementación de los métodos abstractos
    def avanzar(self):
        print("La moto está avanzando.")
    
    def parar(self):
        print("La moto se ha detenido.")
        
class Lancha(Vehiculo):
    def avanzar(self):
        print("La lancha está avanzando.")
    
    def parar(self):
        print("La lancha se ha detenido.")

# Instanciamos la clase Moto
moto = Moto()
barco = Lancha()

# Llamamos a los métodos de la clase Moto
moto.avanzar()
barco.parar()