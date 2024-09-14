# Clases anidadas
#* Anidar clases nos permite tener una clase dentro de otra clase, 
#* esto es útil cuando queremos tener una clase que solo se utilice 
#* en una clase en específico.

class Empresa:
    # Clase anidada
    class Empleado:

        def __init__(self, nombre, posicion):
            self.nombre = nombre
            self.posicion = posicion

        def detalles_empleado(self):
            return f'Nombre: {self.nombre}, Posición: {self.posicion}'
    
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.lista_empleados = []
    
    def contratar_empleado(self, nombre, posicion):
        # Creamos un nuevo empleado
        nuevo_empleado = self.Empleado(nombre, posicion)
        self.lista_empleados.append(nuevo_empleado)
    # Mostramos los empleados
    def mostrar_empleados(self):
        return [empleado.detalles_empleado() for empleado in self.lista_empleados]
    
# Creamos una empresa
compania = Empresa('Google')
# Contratamos empleados
compania.contratar_empleado('Juan', 'Desarrollador')
compania.contratar_empleado('Maria', 'Diseñador')
compania.contratar_empleado('Pedro', 'Contador')

# CREAMOS OTRA INSTANCIA
company = Empresa('Bremen')
# Contratamos empleados
company.contratar_empleado('Alfredo', 'Desarrollador')
company.contratar_empleado('Luis', 'Diseñador')
company.contratar_empleado('Carlos', 'Contador')

# Mostramos los empleados con un ciclo for
for trabajador in compania.mostrar_empleados():
    print(trabajador)
print('-------------------------------')
# Mostramos los empleados con un ciclo for
for trabajador in company.mostrar_empleados():
    print(trabajador)