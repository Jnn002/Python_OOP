# ejemmplo de herencia

# Clase padre
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Clase hijo, hereda de Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
        
# Podemos tener una subclase, que herede una clase hija
# Es decir, podemos tener multiples niveles de herencia
class Chihuahua(Dog):
    pass

# Otra clase hijo, hereda de la clase Animal
class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

# Instancias para nuestras clases
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing inherited methods and attributes
dog.eat()  # Output: Buddy is eating.
cat.eat()  # Output: Whiskers is eating.

dog.bark()  # Output: Buddy is barking.
cat.meow()  # Output: Whiskers is meowing.