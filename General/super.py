#
#* Cuando nuestra herencias necesitan de atributos adicionales o propios
#* debemos crear un constructor en la clase hija, pero al hacer esto
#* se sobreescribe el constructor de la clase padre, por lo que debemos
#* llamar al constructor de la clase padre, para esto usamos la funcion
#* super() que nos permite llamar al constructor de la clase padre
#* tambien podemos usar super() para llamar a metodos de la clase padre

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Clase hija, hereda de Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Uso de super() para llamar al constructor de la clase Animal
        # SE CREA UN CNOSTRUCTOR PARA LA CLASE HIJA PORQUE TIENE ATRIBUTOS ADICIONALES
        # USAMSO SUPER PARA LLAMAR AL CONSTRUCTOR DE LA CLASE PADRE
        # YA QUE EL CONSTRUCTOR DE LA CLASE HIJA, SOBREESCRIBE EL CONSTRUCTOR DE LA CLASE PADRE
        # Y POR ESTO DEBE VOLVER A LLAMARSE, PARA ESTO USAMOS LA FUNCION SUPER()
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name}, the {self.breed}, is barking.")

# Subclase que hereda de Dog (múltiples niveles de herencia)
class Chihuahua(Dog):
    def __init__(self, name):
        # Llama al constructor de Dog con la raza predeterminada "Chihuahua"
        super().__init__(name, breed="Chihuahua")
    
    def bark(self):
        # Podemos extender el método bark usando super()
        # ESTE METODO PERTENECE A LA CLASE PADRE, 
        # PERO LO ESTAMOS SOBREESCRIBIENDO, PARA DISPONER DE EL
        super().bark()
        print(f"{self.name} is a very tiny Chihuahua!")

# Otra clase hija, hereda de la clase Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Llama al constructor de la clase Animal
        self.color = color
    
    def meow(self):
        print(f"{self.name}, the {self.color} cat, is meowing.")

# Instancias para nuestras clases
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "black")
chihuahua = Chihuahua("Pepe")

# Accessing inherited methods and attributes
dog.eat()  # Output: Buddy is eating.
cat.eat()  # Output: Whiskers is eating.
chihuahua.eat()  # Output: Pepe is eating.

dog.bark()  # Output: Buddy, the Labrador, is barking.
cat.meow()  # Output: Whiskers, the black cat, is meowing.
chihuahua.bark()  # Output: Pepe, the Chihuahua, is barking. Pepe is a very tiny Chihuahua!
