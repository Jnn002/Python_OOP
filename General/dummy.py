class Padre():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def caminar():
        pass

class Hijo(Padre):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.nombre = nombre
        self.edad = edad
        
papa = Padre("Juan", 45)
hijo = Hijo('Pedro', 20)
print(papa.nombre)
print(hijo.nombre)