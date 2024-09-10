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

class Carro(Vehiculo):
    def avanzar(self):
        print("El carro está avanzando.")

# No implementamos el método parar
# SI INTENTAMOS INSTANCIAR ESTA CLASE, NOS DARÁ UN ERROR
# TypeError: Can't instantiate abstract class Carro with abstract methods parar
# cuando creamos clases hijas de una clase abstracta, debemos implementar todos 
# los métodos abstractos de la clase padre.

# Instancias de nuestras clases
moto = Moto()
barco = Lancha()
carro = Carro()

# Llamamos a los métodos de la clase Moto
moto.avanzar()
barco.parar()

# No funciará, ya que no implementamos el método parar	en nuestra clase carro
# La clase carro, debe implementar todos los métodos abstractos de la clase padre
#carro.avanzar() 
