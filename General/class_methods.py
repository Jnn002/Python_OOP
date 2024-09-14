# Métodos de clase 
# Los métodos de clase son aquellos que no requieren una instancia de la 
# clase para ser ejecutados, sino que se ejecutan directamente desde la clase.

class Estudiante:
    contador = 0
    general_total_promedio = 0

    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio
        Estudiante.contador += 1
        Estudiante.general_total_promedio += promedio
    
    def mostrar_info(self):
        return f'Estudiante: {self.nombre}, Promedio: {self.promedio}'
    
    @classmethod
    def ver_contador(cls):
        return f'Total de estudiantes: {Estudiante.contador}'
    
    @classmethod
    def ver_promedio(cls):
        if cls.contador == 0:
            return 'No hay estudiantes registrados'
        else:
            return f'Promedio general: {cls.general_total_promedio / cls.contador}'
        
# Instancias de la clase Estudiante
estudiante1 = Estudiante('Juan', 8)
estudiante2 = Estudiante('Karla', 9)
estudiante3 = Estudiante('Pedro', 7)

# Impresión de métodos 
print(Estudiante.ver_contador())
print(Estudiante.ver_promedio())