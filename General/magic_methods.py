# Métodos mágicos en Python
# Los métodos mágicos en Python son aquellos que tienen 
# un doble guion bajo al inicio y al final de su nombre.
#* Estos métodos son llamados automáticamente por Python 
#* dependiendo de la acción que se realice con el objeto.

class Libro:
    
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
    def __str__(self):
        return f'{self.titulo} de {self.autor}'

    # Método mágico para comparar objetos
    def __eq__(self, otro):
        # Compara si 2 libros tienen el mismo autor
        return self.autor == otro.autor
    
    def __gt__(self, otro):
        # Compara si un libro tiene más páginas que otro
        return self.num_paginas > otro.num_paginas
    
    def __contains__(self, palabra):
        # Comprueba si una palabra está en el título del libro
        return palabra in self.titulo
    
    def __getitem__(self, key):
        # Devuelve el valor de un atributo del libro
        if key == 'titulo':
            return self.titulo
        elif key == 'autor':
            return self.autor
        elif key == 'num_paginas':
            return self.num_paginas
        else:
            return f'Error: la clave {key} no existe'
    
libro1 = Libro('El principito', 'Antoine de Saint-Exupéry', 100)
libro2 = Libro('La Odisea', 'Homero', 200)
libro3 = Libro('El señor de los anillos', 'J.R.R. Tolkien', 300)
libro4 = Libro('Cien años de soledad', 'Gabriel García Márquez', 400)
libro5 = Libro('Prueba de método', 'Antoine de Saint-Exupéry', 100)

# compara 2 objetos de la clase Libro si son equivalentes en el paramtro especificado
print(libro1 == libro5) # => True

# compara 2 objetos de la clase Libro si uno es mayor que el otro en el parametro especificado
print(libro1 > libro2) # => False

# Revisa si una cadena está en el título del libro
print('de soledad' in libro4) # => True

# Devuelve el valor de un atributo del libro
print(libro1['titulo']) # => El principito
#print((libro1['editorial'])) # => Error: la clave editorial no existe

#* Los métodos mágicos son muy útiles para personalizar el comportamiento de las clases en Python.
# Los magic methods también se conocen como dunder methods.