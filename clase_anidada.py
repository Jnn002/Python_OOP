# Clases anidadas
#* Anidar clases nos permite tener una clase dentro de otra clase, 
#* esto es útil cuando queremos tener una clase que solo se utilice 
#* en una clase en específico.

class Empresa:
    
    class Empleado:
        def __init__(self, nombre, posicion):
            self.nombre = nombre
            self.posicion = posicion
        
        def detalles_empleado(self):
            return f'Nombre: {self.nombre}, Posición: {self.posicion}'
    
    def __init__(self, nombre_empresa):
        self.nombre = nombre_empresa
        self.lista_empleados = []
    
    def contratar_empleado(self, nombre, posicion):
        empleado = self.Empleado(nombre, posicion)
        self.lista_empleados.append(empleado)
    
    def mostrar_empleados(self):
        return [empleado.detalles_empleado() for empleado in self.lista_empleados]
"""         for empleado in self.lista_empleados:
            print(empleado.detalles_empleado()) """
            
            
company = Empresa('Google')

Empresa.contratar_empleado('Juan', 'Desarrollador', 'test')
""" Empresa.contratar_empleado('Maria', 'Diseñador')
Empresa.contratar_empleado('Pedro', 'Contador') """

#print(Empresa.mostrar_empleados())