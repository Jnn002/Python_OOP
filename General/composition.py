""" 
# Composition en Python
# La composición es una forma de relacionar objetos en la que un 
# objeto contiene a otro objeto y depende de él para existir. 
# En Python, la composición se logra creando instancias de una clase 
# dentro de otra clase.
"""
#? POSEE UN

#
class Biblioteca:
    def __init__(self):
        self.libros = []
    # Método para añadir libros a la biblioteca
    def añadir_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
        else:
            print("Solo se pueden añadir objetos de la clase Libro.")

    # Método para listar los libros de la biblioteca
    def listar_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return "\n".join(str(libro) for libro in self.libros)

# Clase Libro
class Libro:
    def __init__(self, título, autor):
        self.título = título
        self.autor = autor

    def __str__(self):
        return f"{self.título} por {self.autor}"

class Revista:
    def __init__(self, título, autor):
        self.título = título
        self.autor = autor

    def __str__(self):
        return f"{self.título} por {self.autor}"

# Crear instancias de las clases
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
libro3 = Libro("El elefante encadenado", "Jorge Bucay")

revista1 = Revista("Revista 1", "Autor 1")

# Crear una instancia de la clase Biblioteca
biblioteca = Biblioteca()
# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)
biblioteca.añadir_libro(libro3)
# Añadir revista a la biblioteca, rechazado por método de validación
biblioteca.añadir_libro(revista1)

print(biblioteca.listar_libros())

