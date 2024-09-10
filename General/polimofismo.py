# POLIMORFISMO
#* El polimorfismo es la capacidad de un objeto para tomar muchas formas.
#* En Python, el polimorfismo permite a una clase derivada sobrescribir un 
#* método de una clase base. Por lo tanto, una subclase puede definir su
#* propia implementación de un método que ya está definido en su clase base.

from abc import ABC, abstractmethod

class Forma:
    @abstractmethod
    # DEFINICION DE UN MÉTODO ABSTRACTO
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    # IMPLEMENTACION DEL METODO ABSTRACTO DENTRO DE LA CLASE CIRCULO
    def area(self):
        return 3.1416 * (self.radio ** 2)

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    # IMPLEMENTACION DEL METODO ABSTRACTO DENTRO DE LA CLASE CUADRADO
    def area(self):
        return self.lado ** 2

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    # IMPLEMENTACION DEL METODO ABSTRACTO DENTRO DE LA CLASE TRIANGULO
    def area(self):
        return (self.base * self.altura)/2

# Estuvimos trabando con formas sencillaz, pero hagamoslo con algo más
class Mesa(Cuadrado):
    def __init__(self, color, lado):
        super().__init__(lado)
        self.color = color
    # NO NECESITAMOS INSTANCIAR EL METODO AREA, YA QUE LO HEREDAMOS DE LA CLASE PADRE

# Instancias de las clases
# Las 3 clases heredan el método 'area()' de la clase Forma
# Pero cada una de ellas lo implementa de manera diferente
areas = [Circulo(5), Cuadrado(20), Triangulo(7, 9), Mesa('Amarilla', 20) ]
for item in areas:
    print(f'El area total es de: {item.area()}')