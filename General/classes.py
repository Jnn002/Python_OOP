# Clases en Python
# Es un modelo que define un conjunto de atributos 
# y métodos que tendrán los objetos de la clase. Estos 
# pueden ser heredados a subclases

class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.edad = edad
    # Métodos de la clase
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Crear un objeto de la clase Persona
persona1 = Persona('Juan', 30)
persona1.mostrar_datos()


