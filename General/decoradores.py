# Decoradores en Python
#* Los decoradores son funciones que envuelven a otras funciones 
#* o métodos para extender su funcionalidad.

#* Los decoradores nos permiten añadir funcionalidades a una 
#* función sin modificar su código.

class Rectangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura

    # Getter
    @property
    def base(self):
        return f'{self._base:.1f} cm'

    # Getter
    @property
    def altura(self):
        return f'{self._altura:.1f} cm'

    # Setter
    @base.setter
    def base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError('Base debe ser un número positivo')

    # Setter
    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else:
            raise ValueError('Altura debe ser un número positivo')

# Instancia de Rectangulo
fig1 = Rectangulo(10, 20)

# Setter
fig1.base = 20
fig1.altura = 30

# impresión de los valores
print(fig1.base)    
print(fig1.altura)

#* Los decoradores nos permiten agregar lógica adicional a los métodos
#* por ejemplo métodos getter y setter de una clase.