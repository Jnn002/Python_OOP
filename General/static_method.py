# Métodos estáticos
# Estos métodos no reciben ningún argumento especial, 
# como self o cls, y no pueden acceder ni modificar los atributos de la clase.

class Empleado:
    def __init__(self, nombre, posicion):
        self.nombre = nombre
        self.posicion = posicion 
    
    def mostrar_info(self):
        return f'Empleado: {self.nombre}, Posición: {self.posicion}'
    
    # Método estático
    @staticmethod
    def posiciones(posicion):
        # Lista de posiciones disponibles
        posiciones_disp = ['Desarrollador', 'Diseñador', 'Gerente', 'Analista']
        return posicion in posiciones_disp
    
# Instancia de la clase Empleado, evaluamos si laposicion es válida
# con el método estático posiciones
if Empleado.posiciones('Desarrollador'):
    print('Posición válida')
else:
    print('Posición no válida')