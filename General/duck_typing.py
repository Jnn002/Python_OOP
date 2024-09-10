# DUCK TYPING, es otra forma de manejar el polimorfismo en Python
#* Se basa en la idea de que los métodos y atributos de un objeto 
#* son más importantes que su tipo, es decir, si un objeto tiene
#* un método o atributo, entonces se puede utilizar como si fuera

class Animal:
    # Un animal es un ser vivo
    ser_vivo = True

class Perro(Animal):
    # Perro al heredar de Animal, también es un ser vivo
    def hablar(self):
        print('El perro hace guau')

class Gato(Animal):
    # Gato al heredar de Animal, también es un ser vivo
    def hablar(self):
        print('El gato hace miau')
        
class Bicicleta:
    # Bicicleta no hereda de Animal, por lo que no es un ser vivo
    def hablar(self):
        print('La bicicleta no habla')
    ser_vivo = False

animales = [Perro(), Gato(), Bicicleta()]

for x in animales:
    x.hablar()
    print(x.ser_vivo)