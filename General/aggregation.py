# En Python la agregacion es una forma de relacionar objetos,
# en la que un objeto contiene una referencia a otro objeto
# pero no depende de él para existir.
#? TIENE UN

class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    # Método para añadir libros a la librería
    def anadir_libro(self, libro):
        self.libros.append(libro)
    
    # Método para mostrar los libros de la librería
    def mostrar_libros(self):
        return [f'{libro.titulo} - {libro.autor}' for libro in self.libros]

# Clase Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Creacion de instancias de clase Libreria, 
libreria = Libreria("La casa del libro")
libreria2 = Libreria("Librería de la esquina")

# Crear instancias de la clase Libro
libro1 = Libro("El principito", "Antoine de Saint-Exupéry")
libro2 = Libro("El señor de los anillos", "J.R.R. Tolkien")
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")
libro4 = Libro("El retrato de Dorian Gray", "Oscar Wilde")
libro5 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro6 = Libro("La Odisea", "Homero")

# Añadir los libros a la primera librería mediante metodo anadir_libro de la clase Libreria
libreria.anadir_libro(libro1)
libreria.anadir_libro(libro2)
libreria.anadir_libro(libro3)

# Añadir los libros a la seuunda librería mediante metodo anadir_libro de la clase Libreria
libreria2.anadir_libro(libro4)
libreria2.anadir_libro(libro5)
libreria2.anadir_libro(libro6)

# Mostrar los libros de la librería, cargamos los libros de cada librería en una variable
# gracias a metodo mostrar_libros de la clase Libreria
carga = Libreria.mostrar_libros(libreria) # CARGADO CON => EL PRINCIPITO, SEÑOR DE LOS ANILLOS...
carga2 = Libreria.mostrar_libros(libreria2) # CARGADO CON => DORIAN GRAY, CIEN AÑOS DE SOLEDAD...

# Imprimir los libros de la librería
for item in carga2:
    print(item)

# Podemos acceder a cualquier libro de la librería
print('------------')
print(libro5.titulo)